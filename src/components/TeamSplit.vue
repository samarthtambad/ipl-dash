<template>
    <div class="team-split">
        <div class="container">
            <div class="tile is-ancestor">
            <div class="tile">
              <div class="tile is-vertical">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{teamStats.field_first_win_match_perc_avg}}%</p>
                    <p class="subtitle has-text-centered is-size-7">of the times teams that field first ended up winning the match</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{teamStats.toss_win_field_first_perc_avg}}%</p>
                    <p class="subtitle has-text-centered is-size-7">of the times teams that won the toss decided to field first</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">{{teamStats.win_perc_avg}}%</p>
                    <p class="subtitle has-text-centered is-size-7">the percentage of wins of the team {{selected}}</p>
                  </article>
                </div>
              </div>
            </div>
            <div class="tile is-parent is-10">
              <article class="tile is-child box">
                  <div class="tile is-parent">
                    <div class="tile is-8">
                      <p class="subtitle is-size-6 has-text-weight-bold">Season-wise Performance</p>
                    </div>
                    <div class="tile has-text-right">
                      <span>Filter By:  </span>
                      <select id="filter" v-model="selected">
                        <!-- <option disabled value="">Please select one</option> -->
                        <option value="Royal Challengers Bangalore">Royal Challengers Bangalore</option>
                        <option value="Kolkata Knight Riders">Kolkata Knight Riders</option>
                        <option value="Mumbai Indians">Mumbai Indians</option>
                        <option value="Chennai Super Kings">Chennai Super Kings</option>
                        <option value="Rajasthan Royals">Rajasthan Royals</option>
                        <option value="Delhi Daredevils">Delhi Daredevils</option>
                        <option value="Kings XI Punjab">Kings XI Punjab</option>
                        <option value="Deccan Chargers">Deccan Chargers</option>
                        <option value="Pune Warriors">Pune Warriors</option>
                        <option value="Kochi Tuskers Kerala">Kochi Tuskers Kerala</option>
                        <option value="Sunrisers Hyderabad">Sunrisers Hyderabad</option>
                        <option value="Rising Pune Supergiants">Rising Pune Supergiants</option>
                        <option value="Gujarat Lions">Gujarat Lions</option>
                      </select>
                    </div>
                  </div>
                  <line-chart :data="filteredChartData" :label="label"></line-chart>
                </article>
            </div>            
          </div>
        </div>
    </div>
</template>

<script>
import LineChart from "./LineChart"

import seasonList from "../assets/data/json/season_list.json"
import teamData from "../assets/data/json/match_team.json"

export default {
  name: "TeamSplit",
  components: { LineChart },
  data () {
    return {
      data: [10, 17, 12, 14, 15, 16, 12, 11, 10],
      label: "",
      selected: "Royal Challengers Bangalore",
      teamData: teamData,
      seasonList: seasonList,
      filteredData: [],
      teamStats: {}
    }
  },
  computed: {
      filteredChartData: function () {
        this.dataArr = []
        this.filteredData = []
        this.win_perc = []
        this.toss_win_field_first_perc = []
        this.field_first_win_match_perc = []
        teamData.forEach(element => {
            if(element.team == this.selected){
                this.label = this.selected
                this.filteredData.push(element)
                this.dataArr.push(element.wins)
                this.win_perc.push((element.wins/element.matches)*100)
                this.toss_win_field_first_perc.push(element.toss_win_field_first)
                this.field_first_win_match_perc.push(element.field_first_win_match)
            }
        })
        this.teamStats = {}
        this.teamStats['win_perc_avg'] = this.getAvgOfArray(this.win_perc)
        this.teamStats['toss_win_field_first_perc_avg'] = this.getAvgOfArray(this.toss_win_field_first_perc)
        this.teamStats['field_first_win_match_perc_avg'] = this.getAvgOfArray(this.field_first_win_match_perc)
        // correction for missing seasons
        this.i=0
        this.newDataArr = []
        for (let index = 0; index < seasonList.length; index++) {
            if(this.i < this.filteredData.length){
                if(this.filteredData[this.i].season == seasonList[index]){
                    this.newDataArr.push(this.filteredData[this.i].wins)
                    this.i++
                }
                else{
                    this.newDataArr.push(0)
                }
            }
        }
        // console.log(this.filteredData)
        return this.newDataArr
      } 
  },
  methods: {
      getAvgOfArray: function (numArray) {
        this.sum = 0
        numArray.forEach(element => {
          this.sum = this.sum + element
        })
        return Math.round(this.sum/numArray.length)
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