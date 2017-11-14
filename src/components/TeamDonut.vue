<script>
import {Doughnut} from 'vue-chartjs'
export default {
  extends: Doughnut,
  mounted () {
    this.renderChart({
      labels: ['Royal Challengers Bangalore', 'Mumbai Indians', 'Chennai Super Kings', 'Rajasthan Royals', 'Pune Warriors', 'Delhi Daredevils', 'Kings XI Punjab'],
      datasets: [
        {
          backgroundColor: [
            '#41B883',
            '#E46651',
            '#00D8FF',
            '#DD1B16',
            '#FAB42D',
            '#53FA6B',
            '#68AB9C'
          ],
          data: [25, 12, 24, 10, 16, 8, 19]
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
}
</script>