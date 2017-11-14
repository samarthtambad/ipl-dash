<template>
  <div class="home">
    <div class="section">
        <div class="container">
            <div class="tile is-ancestor">
                <div id="team-wins-donut" class="tile is-6">
                  <div class="container">
                    <h1>Matches won split</h1>
                    <team-donut></team-donut>
                  </div>
                </div>
                <div class="tile"></div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import TeamDonut from './TeamDonut'
export default {
  name: 'Home',
  components: { TeamDonut },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
