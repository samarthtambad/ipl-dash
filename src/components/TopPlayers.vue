<template>
    <div class="top-players">
        <div class="container">
            <div class="tile is-ancestor">
            <div class="tile is-6 is-vertical">
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{batsmanStats.max_runs}}</p>
                    <p class="subtitle has-text-centered is-size-7">the maximum number of runs scored by a batsman in season {{selectedforBatsman}}</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{batsmanStats.max_fours}}</p>
                    <p class="subtitle has-text-centered is-size-7">the most number of fours scored by a batsman in season {{selectedforBatsman}}</p>
                  </article>
                </div>
              </div>
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{batsmanStats.max_sixes}}</p>
                    <p class="subtitle has-text-centered is-size-7">the most number of sixes scored by a batsman in season {{selectedforBatsman}}</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{batsmanStats.max_sr}}</p>
                    <p class="subtitle has-text-centered is-size-7">the highest strike rate (SR) among all batsman in season {{selectedforBatsman}}</p>
                  </article>
                </div>
              </div>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <div class="tile is-parent">
                    <div class="tile is-8">
                      <p class="subtitle is-size-6 has-text-weight-bold">Top Batsmen</p>
                    </div>
                    <div class="tile has-text-right">
                      <span>Filter By:  </span>
                      <select id="filter1" v-model="selectedforBatsman">
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
                  </div>
                <table-element :data="filteredBatsmanData" :columns="batsmanColumns"></table-element>
              </article>
            </div>
          </div>

          <div class="tile is-ancestor">
            <div class="tile is-parent">
              <article class="tile is-child box">
                <div class="tile is-parent">
                    <div class="tile is-8">
                      <p class="subtitle is-size-6 has-text-weight-bold">Top Bowlers</p>
                    </div>
                    <div class="tile has-text-right">
                      <span>Filter By:  </span>
                      <select id="filter1" v-model="selectedforBowler">
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
                  </div>
                <table-element :data="filteredBowlerData" :columns="bowlerColumns"></table-element>
              </article>
            </div>
            <div class="tile is-6 is-vertical">
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{bowlerStats.max_wickets}}</p>
                    <p class="subtitle has-text-centered is-size-7">the maximum number of wickets taken by a bowler in season {{selectedforBowler}}</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{bowlerStats.min_avg}}</p>
                    <p class="subtitle has-text-centered is-size-7">the best bowling average among all bowlers in season {{selectedforBowler}}</p>
                  </article>
                </div>
              </div>
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{bowlerStats.min_econ}}</p>
                    <p class="subtitle has-text-centered is-size-7">the best economy rate among all bowlers in season {{selectedforBowler}}</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{bowlerStats.min_runs}}</p>
                    <p class="subtitle has-text-centered is-size-7">the least number of runs conceded by a bowler in season {{selectedforBowler}}</p>
                  </article>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
</template>

<script>
import TableElement from "./TableElement"

import seasonList from "../assets/data/json/season_list.json"
import batsmanData from "../assets/data/json/batsmen.json"
import bowlerData from "../assets/data/json/bowlers.json"


export default {
  name: "TopPlayers",
  components: { TableElement },
  data () {
    return {
      selectedforBatsman: "1",
      selectedforBowler: "1",
      seasonList: seasonList,
      batsmanData: batsmanData,
      bowlerData: bowlerData,
      batsmanStats: {},
      bowlerStats: {},
      batsmanColumns: ['batsman', 'matches', 'balls_faced', 'batsman_runs', '4s', '6s', 'Avg', 'SR'],
      bowlerColumns: ['bowler', 'matches', 'over', 'runs', 'wickets', 'Econ', 'Avg'],
    }
  },
  computed: {
      filteredBatsmanData: function () {
        this.filteredData = []
        this.fours = []
        this.sixes = []
        this.sr = []
        this.runs = []
        batsmanData.forEach(element => {
            if(element.season == seasonList[this.selectedforBatsman-1]){
              this.filteredData.push(element)
              this.fours.push(element["4s"])
              this.sixes.push(element["6s"])
              this.sr.push(element["SR"])
              this.runs.push(element["batsman_runs"])
            }
        })
        this.batsmanStats = {}
        this.batsmanStats["max_fours"] = this.getMaxOfArray(this.fours)
        this.batsmanStats["max_sixes"] = this.getMaxOfArray(this.sixes)
        this.batsmanStats["max_sr"] = this.getMaxOfArray(this.sr)
        this.batsmanStats["max_runs"] = this.getMaxOfArray(this.runs)
        // console.log(this.batsmanStats)
        // console.log(this.filteredData)
        return this.filteredData
      },
      filteredBowlerData: function () {
        this.filteredData = []
        this.wickets = []
        this.econ = []
        this.avg = []
        this.runs = []
        bowlerData.forEach(element => {
            if(element.season == seasonList[this.selectedforBowler-1]){
              this.filteredData.push(element)
              this.wickets.push(element["wickets"])
              this.econ.push(element["Econ"])
              this.avg.push(element["Avg"])
              this.runs.push(element["runs"])
            }
        })
        this.bowlerStats = {}
        this.bowlerStats["max_wickets"] = this.getMaxOfArray(this.wickets)
        this.bowlerStats["min_econ"] = this.getMinOfArray(this.econ)
        this.bowlerStats["min_avg"] = this.getMinOfArray(this.avg)
        this.bowlerStats["min_runs"] = this.getMinOfArray(this.runs)
        // console.log(this.bowlerStats)
        // console.log(this.filteredData)
        return this.filteredData
      }
  },
  methods: {
      getMaxOfArray: function (numArray) {
          return Math.max.apply(null, numArray)
      },
      getMinOfArray: function (numArray) {
          return Math.min.apply(null, numArray)
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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