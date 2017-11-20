<template>
  <div class="home">
    <div class="section">
        <div class="container">

          <div class="tile is-ancestor">
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title has-text-centered is-size-1">60%</p>
                <p class="subtitle has-text-centered is-size-7">of the toss winners chose to field first</p>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title has-text-centered is-size-1">4</p>
                <p class="subtitle has-text-centered is-size-7">average number of balls between each boundary</p>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title has-text-centered is-size-1">70%</p>
                <p class="subtitle has-text-centered is-size-7">of the times the team chasing won the match</p>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title has-text-centered is-size-1">30%</p>
                <p class="subtitle has-text-centered is-size-7">of the all dismissals were due to catches</p>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title has-text-centered is-size-1">30%</p>
                <p class="subtitle has-text-centered is-size-7">of the all dismissals were due to catches</p>
              </article>
            </div>
          </div>

          <!-- <div class="tile is-ancestor">
            <div class="tile is-parent">
              <article class="tile is-child box">
                
                <div class="tile is-parent">
                  <span>Filter By:  </span>
                  <select id="filter1" v-model="selected" v-on:change="onFilterChange">
                    <option disabled value="">Please select one</option>
                    <option>All Seasons</option>
                    <option>Season 1</option>
                    <option>Season 2</option>
                    <option>Season 3</option>
                    <option>Season 4</option>
                    <option>Season 5</option>
                    <option>Season 6</option>
                    <option>Season 7</option>
                    <option>Season 8</option>
                    <option>Season 9</option>
                    <option>Season 10</option>
                  </select>
                </div>

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
                      <donut-chart :chartData="donutData" :options="chartOptionsDonut"></donut-chart>
                    </article>
                  </div>
                </div>
              </article>
            </div>
          </div> -->
          
          <season-split></season-split>

          <div class="tile is-ancestor">
            <div class="tile">
              <div class="tile is-vertical">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">60%</p>
                    <p class="subtitle has-text-centered is-size-7">of the toss winners chose to field first</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">4</p>
                    <p class="subtitle has-text-centered is-size-7">average number of balls between each boundary</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">70%</p>
                    <p class="subtitle has-text-centered is-size-7">of the times the team chasing won the match</p>
                  </article>
                </div>
              </div>
            </div>
            <div class="tile is-parent is-10">
              <article class="tile is-child box">
                  <div class="tile is-parent">
                    <div class="tile is-10">
                      <p class="subtitle is-size-6 has-text-weight-bold">Season-wise Performance</p>
                    </div>
                    <div class="tile has-text-right">
                      <span>Filter By:  </span>
                      <select id="filter">
                        <option>RCB</option>
                        <option>KKR</option>
                        <option>MI</option>
                        <option>CSK</option>
                        <option>RR</option>
                        <option>DD</option>
                        <option>KXIP</option>
                        <option>DC</option>
                        <option>PW</option>
                        <option>KTK</option>
                        <option>SH</option>
                        <option>RPS</option>
                        <option>GL</option>
                      </select>
                    </div>
                  </div>
                  <line-chart :chartData="lineData" :options="chartOptions"></line-chart>
                </article>
            </div>            
          </div>

          <div class="tile is-ancestor">
            <div class="tile is-6 is-vertical">
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">60%</p>
                    <p class="subtitle has-text-centered is-size-7">of the toss winners chose to field first</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">4</p>
                    <p class="subtitle has-text-centered is-size-7">average number of balls between each boundary</p>
                  </article>
                </div>
              </div>
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">60%</p>
                    <p class="subtitle has-text-centered is-size-7">of the toss winners chose to field first</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">4</p>
                    <p class="subtitle has-text-centered is-size-7">average number of balls between each boundary</p>
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
                      <select id="filter">
                        <option>All Seasons</option>
                        <option>Season 1</option>
                        <option>Season 2</option>
                        <option>Season 3</option>
                        <option>Season 4</option>
                        <option>Season 5</option>
                        <option>Season 6</option>
                        <option>Season 7</option>
                        <option>Season 8</option>
                        <option>Season 9</option>
                        <option>Season 10</option>
                      </select>
                    </div>
                  </div>
                <table-element :data="batsmenData" :columns="batsmenColumns"></table-element>
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
                      <select id="filter">
                        <option>All Seasons</option>
                        <option>Season 1</option>
                        <option>Season 2</option>
                        <option>Season 3</option>
                        <option>Season 4</option>
                        <option>Season 5</option>
                        <option>Season 6</option>
                        <option>Season 7</option>
                        <option>Season 8</option>
                        <option>Season 9</option>
                        <option>Season 10</option>
                      </select>
                    </div>
                  </div>
                <table-element :data="batsmenData" :columns="batsmenColumns"></table-element>
              </article>
            </div>
            <div class="tile is-6 is-vertical">
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">60%</p>
                    <p class="subtitle has-text-centered is-size-7">of the toss winners chose to field first</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">4</p>
                    <p class="subtitle has-text-centered is-size-7">average number of balls between each boundary</p>
                  </article>
                </div>
              </div>
              <div class="tile">
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">60%</p>
                    <p class="subtitle has-text-centered is-size-7">of the toss winners chose to field first</p>
                  </article>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="title has-text-centered is-size-1">4</p>
                    <p class="subtitle has-text-centered is-size-7">average number of balls between each boundary</p>
                  </article>
                </div>
              </div>
            </div>
          </div>
          
        </div>
    </div>
  </div>
</template>

<script>
import DonutChart from "./DonutChart";
import LineChart from "./LineChart";
import TableElement from "./TableElement";
import SeasonSplit from "./SeasonSplit";

import teamList from "../assets/data/processed/data/teamList.json";
import teamData from "../assets/data/processed/data/teams.json";
console.log(this.$refs);

export default {
  name: "Home",
  components: { DonutChart, LineChart, TableElement, SeasonSplit },
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      selected: "",
      teamList: teamList,
      teamData: teamData,
      donutData: {
        labels: [
          "Royal Challengers Bangalore",
          "Kolkata Knight Riders",
          "Mumbai Indians",
          "Chennai Super Kings",
          "Rajasthan Royals",
          "Delhi Daredevils",
          "Kings XI Punjab",
          "Deccan Chargers",
          "Pune Warriors",
          "Kochi Tuskers Kerala",
          "Sunrisers Hyderabad",
          "Rising Pune Supergiants",
          "Gujarat Lions"
        ],
        datasets: [
          {
            backgroundColor: [
              "#ED5F5A",
              "#70FFA0",
              "#CCCCCC",
              "#EA8CFF",
              "#47C2FF",
              "#F4F78F",
              "#4893B2",
              "#FECEB5",
              "#2B9E86",
              "#D38E7D",
              "#B1FFFF",
              "#A26B28",
              "#003468"
            ],
            cutoutPercentage: 0,
            label: "RCB",
            data: [25, 12, 24, 12, 43, 32, 21, 25, 12, 24, 43, 32, 21]
          }
        ]
      },
      lineData: {
        labels: [
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017"
        ],
        datasets: [
          {
            label: "Royal Challengers Bangalore",
            backgroundColor: "#ED5F5A",
            borderColor: "#ED5F5A",
            fill: false,
            data: [25, 12, 24, 10, 16, 8, 19, 21, 15, 11]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false,
          position: "right",
          labels: {
            boxWidth: 12,
            fontSize: 10,
            usePointStyle: true
          }
        },
        tooltips: {
          intersect: false
        },
        scales: {
          xAxes: [
            {
              id: "x-axis",
              scaleLabel: {
                display: true,
                labelString: "Season"
              }
            }
          ],
          yAxes: [
            {
              id: "y-axis",
              scaleLabel: {
                display: true,
                labelString: "Wins"
              }
            }
          ]
        }
      },
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
      batsmenColumns: ["Pos", "Player", "Matches", "Runs", "Avg", "SR"],
      batsmenData: [
        {
          Pos: 1,
          Player: "Virat Kohli",
          Runs: 120
        },
        {
          Pos: 2,
          Player: "Suresh Raina",
          Runs: 100
        },
        {
          Pos: 3,
          Player: "Virat Kohli",
          Runs: 120
        },
        {
          Pos: 4,
          Player: "Suresh Raina",
          Runs: 100
        },
        {
          Pos: 5,
          Player: "Virat Kohli",
          Runs: 120
        }
      ],
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
    };
  }
};
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
