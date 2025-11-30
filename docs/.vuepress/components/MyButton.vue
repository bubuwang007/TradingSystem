<template>
  <div>
    <button class="my-btn">
      <slot />
    </button>
  </div>
</template>

<style>
.my-btn {
  padding: 8px 16px;
  background: #42b983;
  color: white;
  border-radius: 6px;
}
</style>
