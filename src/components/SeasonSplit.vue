<template>
    <div class="season-split">
        <div class="container">
        <div class="tile is-ancestor">
            <div class="tile is-parent">
                <article class="tile is-child box">
                    <div class="tile is-parent">
                        <span>Filter By:  </span>
                        <select id="filter1" v-model="selected" v-on:change="onFilterChanged()">
                        <option disabled value="">Please select one</option>
                        <option value="0" selected>All Seasons</option>
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
                    <div> {{filteredTeamsData}} {{selected}} {{chartData}}</div>
                    <div class="tile">
                        <div class="tile is-parent is-6">
                            <article class="tile is-child ">
                                <p class="subtitle is-size-6 has-text-weight-bold">Points Table</p>
                                <table-element :data="pointsData" :columns="pointsColumns"></table-element>
                            </article>
                        </div>
                        <div class="tile is-parent">
                            <article class="tile is-child ">
                                <p class="subtitle is-size-6 has-text-weight-bold">Number of wins of each team</p>
                                <donut-chart :data="chartData" :options="chartOptionsDonut" :labels="teamList"></donut-chart>
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

import teamList from "../assets/data/processed/data/teamList.json"
import teamData from "../assets/data/processed/data/teams.json"

export default {
  name: "SeasonSplit",
  components: { DonutChart, TableElement },
  data () {
    return {
      selected: "",
      teamData: teamData,
      teamList: teamList,
      tableData: [],
      chartData: [12],
      chartOptionsDonut: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: true,
          position: "right",
          labels: {
            boxWidth: 12,
            fontSize: 10,
            usePointStyle: true
          }
        }
      },
      donutData: {},
      pointsColumns: ["Pos", "Team", "Matches", "Win", "Loss", "Tie", "Pts"],
      pointsData: [
        {
          Pos: 1,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 2,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 3,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 4,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 5,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 6,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 7,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 8,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 9,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 10,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 11,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 12,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        },
        {
          Pos: 13,
          Team: "RCB",
          Matches: 120,
          Win: 68,
          Loss: 47,
          Tie: 5,
          Pts: 130
        }
      ]
    }
  },
    computed: {
        filteredTeamsData: function () {
            this.temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            teamList.forEach(element => {
                this.temp[this.selected - 1] = teamData[element].totalMatchPlayed[this.selected]
                // this.temp.push(teamData[element].totalMatchPlayed[this.selected])
            })
            return this.temp
        }
    },
    methods: {
        onFilterChanged: function () {
            this.temp = []
            teamList.forEach(element => {
                this.temp.push(teamData[element].matchWon[this.selected])
            })
            this.chartData = this.temp
            
            this.tableTemp = []
            teamList.forEach(element => {
                this.tableDict = {}
                this.tableDict['Team'] = teamData[element].matchWon[this.selected]
                this.tableDict['Matches'] = teamData[element].totalMatchPlayed[this.selected]
                this.tableDict['Win'] = teamData[element].matchWon[this.selected]
                this.tableDict['Loss'] = teamData[element].matchWon[this.selected]
                this.tableDict['Tie'] = teamData[element].matchWon[this.selected]
                this.tableDict['Pts'] = teamData[element].matchWon[this.selected]
                this.tableDict['Team'] = teamData[element].matchWon[this.selected]
                this.tableTemp.push(teamData[element].matchWon[this.selected])
            })
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