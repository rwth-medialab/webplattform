<template>
  <div class="form-group">
    <label :for="id">{{ label }}:<span v-if="required">*</span></label>
    <div class="d-flex">
    <input :type="type" class="form-control" :class="{'form__field--error': error}" :id="id" :placeholder="placeholder" v-model="inputValue" :readonly="readonly" :maxlength="maximalChars">
    <button class="button--neutral button--smallSquare button--help ml-1" type="button" data-toggle="tooltip" data-placement="top" :title="helpText" v-if="helpText"></button>
    </div>
    <small v-if="characterCounter" class="form-text text-muted float-right">{{ charactersLeft }} Zeichen verbleibend</small>
    <div class="clearfix"></div>
    <app-review-input :mode="review ? 'review' : 'edit'" :id="'id'+-review" :name="label" :reviewValue.sync="ownReviewValue"></app-review-input>
  </div>
</template>

<script>
  import ReviewInput from './ReviewInput.vue'
  import { reviewMixin } from '../mixins/reviewMixin'

  export default {
    name: 'TextInput',
    components: {
      'AppReviewInput': ReviewInput
    },
    mixins: [reviewMixin],
    props: {
      id: {
        type: String,
        default: '',
        required: true
      },
      type: {
        type: String,
        default: 'text',
        required: false
      },
      readonly: {
        type: Boolean,
        default: false,
        required: false
      },
      placeholder:{
        type: String,
        default: '',
        required: false
      },
      characterCounter: {
        type: Boolean,
        default: false,
        required: false
      },
      maximalChars: {
        type: Number,
        default: null,
        required: false
      },
      required: {
        type: Boolean,
        default: false,
        required: false
      },
      label: {
        type: String,
        default: '',
        required: true
      },
      value: {
        type: String,
        default: '',
        required: false
      },
      helpText: {
        type: String,
        default: '',
        required: false
      },
      error: {
        type: Boolean,
        default: false,
        required: false
      }
    },
    computed: {
      charactersLeft () {
        return this.value ? this.maximalChars - this.value.length : this.maximalChars
      }
    },
    data () {
      return {
        inputValue: ''
      }
    },
    created () {
      this.inputValue = this.value
    },
    watch: {
      inputValue (newValue) {
        this.$emit('update:value', newValue)
      }
    }
  }
</script>

<style scoped>

</style>