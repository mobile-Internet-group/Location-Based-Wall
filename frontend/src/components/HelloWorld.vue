<template>
  <div class="hello">
    <h1 >{{ msg }}</h1>
    <ul>
      <li v-for= "(wall,index) in walls" :key="index" style="display:block">
        {{index}}-{{wall.name}}-{{wall.author}}
      </li>
    </ul>

    <form action="">
      输入标题:<input type="text" placeholder="wall name" v-model="inputWall.name"><br>
      输入作者":<input type="text" placeholder="wall author" v-model="inputWall.author"><br>
    </form>
    
    <button type="submit" @click="wallSubmit()"> submit </button>

  </div>
</template>

<script>
import { setTransitionHooks } from 'vue';
import {getWalls,postWall} from '../api/api.js'
defineProps({
  msg: {
    type: String,
    required: true
}})

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      // books list data
      walls: [
        {name: 'test1', author: 't1'},
        {name: 'test2', author: 't2'}
      ],
      // book data in the form
      inputWall: {
        "name": "",
        "author": "",
      }
    }
  },
  methods: {
    loadWalls () {
      getWalls().then(response =>{
        this.walls = response.data
      })
    }, // load walls list when visit the page
    wallSubmit () {
      postWall(this.inputWall.name,this.inputWall.author).then(response=>{
        console.log(response)
        setTransitionHooks.loadWalls()
      })
    } // add a wall to backend when click the button
  },
  created: function () {
    this.loadWalls()
  }
}
</script>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
