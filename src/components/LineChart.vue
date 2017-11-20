<script>

import {Line} from 'vue-chartjs'

export default {
  extends: Line,
  props: ['data', 'options', 'label'],
  mounted () {
    this.renderLineChart()
  },
  computed: {
    chartData: function() {
      return this.data;
    }
  },
  methods: {
    renderLineChart: function () {
      this.renderChart(
        {
          labels: [
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016"
          ],
          datasets: [
            {
              label: this.label,
              backgroundColor: "#ED5F5A",
              borderColor: "#ED5F5A",
              fill: false,
              data: this.data
            }
          ]
        }, 
        {
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
      });
    }
  },
  watch: {
    data: function() {
      // console.log(this)
      this.$data._chart.destroy()
      //this.renderChart(this.data, this.options);
      this.renderLineChart()
    }
  }
}
</script>