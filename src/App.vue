<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <header class="navbar is-dark" role="navigation" aria-label="main navigation">
      <div class="container">
        <div class="navbar-brand">
          <h1 class="navbar-item">IPL Dashboard</h1>
        </div>
      </div>
    </header>
    <router-view class="view"/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
  
</style>
