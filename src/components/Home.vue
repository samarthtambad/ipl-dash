<template>
  <div class="home">
    <div class="section">
        <div class="container">
          <season-split></season-split>
          <team-split></team-split>
          <top-players></top-players>
        </div>
    </div>
  </div>
</template>

<script>
import SeasonSplit from "./SeasonSplit";
import TeamSplit from "./TeamSplit";
import TopPlayers from "./TopPlayers";

export default {
  name: "Home",
  components: { SeasonSplit, TeamSplit, TopPlayers },
  data() {
    return {
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
