<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <header class="navbar is-dark" role="navigation" aria-label="main navigation">
      <div class="container">
        <div class="navbar-brand">
          <h1 class="navbar-item">IPL Dashboard</h1>
          <button class="button navbar-burger is-dark">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
        <div class="navbar-menu">
          <div class="navbar-end">
            <router-link class="navbar-item" to="/">Home</router-link>
            <router-link class="navbar-item" to="/teams">Teams</router-link>
            <router-link class="navbar-item" to="/players">Players</router-link>
            <router-link class="navbar-item" to="/facts">Fun Facts</router-link>
          </div>
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
