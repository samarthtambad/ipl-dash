<template>
    <div class="season-split">
        <div class="container">
            <div class="tile is-ancestor margin-correction">
                <div class="tile is-parent">
                    <article class="tile is-child box">
                        <div class="tile is-parent">
                            <span>Filter By:  </span>
                            <select id="filter1" v-model="selected">
                            <!-- <option disabled value="">Please select one</option> -->
                            <option value="1">Season 1</option>
                            <option value="2">Season 2</option>
                            <option value="3">Season 3</option>
                            <option value="4">Season 4</option>
                            <option value="5">Season 5</option>
                            <option value="6">Season 6</option>
                            <option value="7">Season 7</option>
                            <option value="8">Season 8</option>
                            <option value="9">Season 9</option>
                            </select>
                        </div>
                        <div class="tile">
                            <div class="tile is-parent is-6">
                                <article class="tile is-child ">
                                    <p class="subtitle is-size-6 has-text-weight-bold">Points Table</p>
                                    <table-element :data="filteredData" :columns="tableColumns"></table-element>
                                </article>
                            </div>
                            <div class="tile is-parent">
                                <article class="tile is-child ">
                                    <p class="subtitle is-size-6 has-text-weight-bold">Win split of each team</p>
                                    <donut-chart :data="filteredTeamsData" :labels="teamList"></donut-chart>
                                </article>
                            </div>
                        </div>
                    </article>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import DonutChart from "./DonutChart"
import TableElement from "./TableElement"

import seasonList from "../assets/data/json/season_list.json"
import teamData from "../assets/data/json/match_team.json"

export default {
  name: "SeasonSplit",
  components: { DonutChart, TableElement },
  data () {
    return {
      selected: "1",
      teamData: teamData,
      teamList: [],
      seasonList: seasonList,
      filteredData: [],
      tableColumns: ['team', 'matches', 'wins', 'losses', 'pts']
    }
  },
  computed: {
      filteredTeamsData: function () {
        this.dataArr = []
        this.filteredData = []
        this.teamList = []
        teamData.forEach(element => {
            if(element.season == seasonList[this.selected-1]){
              this.filteredData.push(element)
              this.teamList.push(element.team)
              this.dataArr.push(element.wins)
            }
        })
        // console.log(this.filteredData)
        return this.dataArr
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .margin-correction{
    margin-bottom: 0.75em !important;
  }
  select {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border: none;
    outline: none;
    color: #4a4a4a;
    font-weight: bold;
    border-radius: 0;
    border-bottom: 2px solid #4a4a4a;
    background-color: transparent;
    font-size: 0.9rem;
    text-align: center;
    margin-left: 0.5rem;
  }
</style>