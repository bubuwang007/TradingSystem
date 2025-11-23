from logging import getLogger
def verify_cookies(self) -> bool:
        """验证 cookies 有效性"""
        if not self.cookies:
            logger.warning("没有 cookies 可验证")
            return False

        session = requests.Session()
        session.cookies.update(self.cookies)
        session.headers.update(DEFAULT_HEADERS)

        try:
            response = session.get('https://www.eastmoney.com/', timeout=10)
            if response.status_code == 200 and '拒绝访问' not in response.text:
                logger.info("✓ Cookies 验证成功")
                return True
            else:
                logger.warning(f"Cookies 验证失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.warning(f"Cookies 验证失败: {e}")
            return False

    def create_session(self) -> requests.Session:
        """创建带 cookies 的会话"""
        if not self.cookies:
            self.load_cookies()

        session = requests.Session()
        session.cookies.update(self.cookies)
        session.headers.update(DEFAULT_HEADERS)

        # 设置更合理超时和重试策略
        session.mount('http://', HTTPAdapter(max_retries=3))
        session.mount('https://', HTTPAdapter(max_retries=3))

        return session

    def patch_requests(self, session: requests.Session):
        """修补 requests 模块，使其使用我们的会话"""
        # 保存原始方法
        if not self.original_requests_get:
            self.original_requests_get = requests.get
            self.original_requests_post = requests.post

        # 定义新的请求方法
        def patched_get(url, **kwargs):
            # 确保使用我们的会话
            kwargs.pop('session', None)

            # 添加超时设置
            if 'timeout' not in kwargs:
                kwargs['timeout'] = (10, 30)

            try:
                response = session.get(url, **kwargs)

                # 检查响应内容
                if response.status_code != 200:
                    logger.warning(f"请求失败: {url} - 状态码: {response.status_code}")

                return response

            except Exception as e:
                logger.error(f"请求失败: {url} - {e}")
                raise

        def patched_post(url, **kwargs):

            kwargs.pop('session', None)
            if 'timeout' not in kwargs:
                kwargs['timeout'] = (10, 30)
            return session.post(url, **kwargs)

        # 应用修补
        requests.get = patched_get
        requests.post = patched_post

    def restore_requests(self):
        """恢复原始 requests 方法"""
        if self.original_requests_get:
            requests.get = self.original_requests_get
            requests.post = self.original_requests_pos