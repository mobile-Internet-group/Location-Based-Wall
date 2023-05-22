<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <!-- show books list -->
    <ul>
      <li v-for="(wall, index) in walls" :key="index" style="display:block">
        {{index}}-{{wall.name}}-{{wall.author}}
      </li>
    </ul>
    <!-- form to add a book -->
    <form action="">
      输入题目：<input type="text" placeholder="wall name" v-model="inputWall.name"><br>
      输入作者：<input type="text" placeholder="wall author" v-model="inputWall.author"><br>
    </form>
    <button type="submit" @click="bookSubmit()">submit</button>
  </div>
</template>

<script>
import {getWalls, postWall} from '../api/api.js'
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
      getWalls().then(response => {
        this.books = response.data
      })
    }, // load books list when visit the page
    wallSubmit () {
      postWall(this.inputBook.name, this.inputBook.author).then(response => {
        console.log(response)
        this.loadBooks()
      })
    } // add a book to backend when click the button
  },
  created: function () {
    this.loadWalls()
  }
}
</script>
<!-- <script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      You’ve successfully created a project with
      <a href="https://vitejs.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>.
    </h3>
  </div>
</template>

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
</style> -->
