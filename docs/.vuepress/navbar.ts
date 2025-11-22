/**
 * @see https://theme-plume.vuejs.press/config/navigation/ 查看文档了解配置详情
 *
 * Navbar 配置文件，它在 `.vuepress/plume.config.ts` 中被导入。
 */

import { defineNavbarConfig } from "vuepress-theme-plume";

export default defineNavbarConfig([
  { text: "首页", link: "/" },
  { text: "知识体系", link: "/知识体系/"},
  { text: "A股", link: "/A股/" },
  { text: "期货", link: "/期货/" },
  { text: "美股", link: "/美股/" },
  { text: "外汇", link: "/外汇/" },
  { text: "虚拟货币", link: "/虚拟货币/" },
  { text: "我的交易", link: "/我的交易/" },
]);
