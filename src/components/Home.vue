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

          <div class="tile is-ancestor">
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="subtitle is-size-6 has-text-weight-bold">Points Table</p>
                <table-element :data="pointsData" :columns="pointsColumns"></table-element>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="subtitle is-size-6 has-text-weight-bold">Number of wins of each team</p>
                <donut-chart :chartData="donutData" :options="chartOptions"></donut-chart>
              </article>
            </div>
          </div>
          
          <div class="tile is-ancestor">
            <div class="tile is-7 is-vertical">
              <div class="tile">
                <!-- <div class="tile is-4 is-vertical">
                  <div class="tile is-parent">
                    <article class="tile is-child box">
                      
                    </article>
                  </div>
                  <div class="tile is-parent">
                    <article class="tile is-child box">
                      
                    </article>
                  </div>
                </div> -->
                <div class="tile is-parent">
                  <article class="tile is-child box">
                    <p class="subtitle has-text-centered">Top Bowlers</p>
                    <donut-chart :chartData="donutData" :options="chartOptions"></donut-chart>
                    <!-- <line-chart :chartData="lineData" :options="chartOptions"></line-chart> -->
                  </article>
                </div>
              </div>
              <div class="tile is-parent">
                <article class="tile is-child box">
                  <line-chart :chartData="lineData" :options="chartOptions"></line-chart>
                  <!-- <donut-chart :chartData="donutData" :options="chartOptions"></donut-chart> -->
                </article>
              </div>
            </div>
            <div class="tile">
              <!-- <article class="tile is-child box"> -->
                  <div class="tile is-parent is-vertical">
                    <article class="tile is-child box">
                        <p class="subtitle has-text-centered">Top Batsmen</p>
                        <table-element :data="batsmenData" :columns="batsmenColumns"></table-element>
                    </article>
                    <article class="tile is-child box">
                        <p class="subtitle has-text-centered">Top Bowlers</p>
                        <table-element :data="batsmenData" :columns="batsmenColumns"></table-element>
                    </article>
                  </div>
              <!-- </article> -->
            </div>
          </div>
          
        </div>
    </div>
  </div>
</template>

<script>
import DonutChart from './DonutChart'
import LineChart from './LineChart'
import TableElement from './TableElement'

export default {
  name: 'Home',
  components: { DonutChart, LineChart, TableElement },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      donutData: {
        labels: ['Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Mumbai Indians', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Daredevils', 'Kings XI Punjab', 'Deccan Chargers', 'Pune Warriors', 'Kochi Tuskers Kerala', 'Sunrisers Hyderabad', 'Rising Pune Supergiants', 'Gujarat Lions'],
        datasets: [
          {
            backgroundColor: [
              '#ED5F5A',
              '#70FFA0',
              '#CCCCCC',
              '#EA8CFF',
              '#47C2FF',
              '#F4F78F',
              '#4893B2',
              '#FECEB5',
              '#2B9E86',
              '#D38E7D',
              '#B1FFFF',
              '#A26B28',
              '#003468'
            ],
            cutoutPercentage: 0,
            label: 'RCB',
            data: [25, 12, 24, 12, 43, 32, 21, 25, 12, 24, 43, 32, 21]
          }
        ]
      },
      lineData: {
        labels: ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
        datasets: [
          {
            label: 'Royal Challengers Bangalore',
            backgroundColor: '#ED5F5A',
            borderColor: '#ED5F5A',
            fill: false,
            data: [25, 12, 24, 10, 16, 8, 19, 21, 15, 11]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        responsive: true,
        legend: {
          display: true,
          position: 'right',
          labels: {
            boxWidth: 12,
            fontSize: 10,
            usePointStyle: true
          }
        },
        tooltips: {
          intersect: false
        }
      },
      batsmenColumns: ['Pos', 'Player', 'Matches', 'Runs', 'Avg', 'SR'],
      batsmenData: [
        {
          Pos: 1,
          Player: 'Virat Kohli',
          Runs: 120
        },
        {
          Pos: 2,
          Player: 'Suresh Raina',
          Runs: 100
        },
        {
          Pos: 3,
          Player: 'Virat Kohli',
          Runs: 120
        },
        {
          Pos: 4,
          Player: 'Suresh Raina',
          Runs: 100
        },
        {
          Pos: 5,
          Player: 'Virat Kohli',
          Runs: 120
        }
      ],
      pointsColumns: ['Pos', 'Team', 'Matches', 'Wins', 'Losses', 'Draw', 'Points'],
      pointsData: [
        {
          Pos: 1,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 2,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 3,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 4,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 5,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 6,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 7,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 8,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 9,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 10,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 11,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 12,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        },
        {
          Pos: 13,
          Team: 'Royal Challengers Bangalore',
          Matches: 120,
          Wins: 68,
          Losses: 47,
          Draw: 5,
          Points: 130
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
