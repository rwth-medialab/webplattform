import $ from 'jquery'
import axios from 'axios'

class Trigger {
  constructor(type, delay, survey, url) {
    this.delay = delay
    this.url = url
    this.type = type
    this.survey = survey
    this.getSurveyContent().then((res) => {
      this.html = res.data
      this.setup()
    })
  }
  listenerFunc () {
    if (this.type === 'leaveIntent') {
      document.removeEventListener('mouseleave', this.listenerFunc)
    }
    setTimeout(() => {
      var modal = $('.js-surveyModal').modal()
      modal.find('.modal-body').html(this.html)
      modal.show()
    }, this.delay)
  }

  setup() {
    $('.js-surveyModal').on('submit', 'form', (e) => {
      e.preventDefault()
      axios.post(`/surveys/${this.survey}`, $(e.target).serialize()).then(res => {
        var modal = $('.js-surveyModal').modal()
        if (!res.data.success) {
          this.html = res.data.form
          modal.find('.modal-body').html(this.html)
        } else {
          modal.modal('hide')
        }
      }).catch(err => {
        console.log(err)
      })
      return false
    })
    if (this.type === 'leaveIntent' && window.location.pathname === this.url) {
      document.addEventListener('mouseleave', this.listenerFunc)
      return
    }
    if (this.type === 'pageOpen' && window.location.pathname === this.url) {
      this.listenerFunc()
      return
    }
    window.addEventListener(this.type, this.listenerFunc)
  }

  getSurveyContent() {
    return axios.get(`/surveys/${this.survey}`)
  }
}

window.Trigger = Trigger
