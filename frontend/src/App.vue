<script setup>
import { ref } from 'vue'

const name = ref('')
const feeling = ref('')
const affirmation = ref('')
const loading = ref(false)
const error = ref('')

async function submitForm() {
  error.value = ""
  affirmation.value = ""
  loading.value = true

  try {
    const response = await fetch("http://localhost:8000/api/affirmation/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name.value,
        feeling: feeling.value
      })
    })

    const data = await response.json()

    if (response.ok) {
      affirmation.value = data.affirmation 
    } else {
      error.value = data.error || "Something went wrong"
    }
  } catch (err) {
    error.value = "Failed to connect to server"
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <h1>Mood Architect</h1>
  <section>
    <form @submit.prevent="submitForm" class="card">
      <h2>Welcome to Marisa Peers Mood Architect!</h2>

      <label for="name">What is your name?</label>
      <input type="text" id="name" v-model="name">

      <label for="feeling">Describe how you are feeling:</label>
      <textarea rows="5" id="feeling" v-model="feeling"></textarea>

      <button class="btn" type="submit">Submit</button>
    </form>

    <div class="card">
      <p v-if="loading">Generating response...</p>
      <p v-else-if="affirmation">{{ affirmation }}</p>
      <p v-else>Response will appear here</p>
    </div>
  </section>
</template>

<style>
:root {
  --text-light: white;
  --text-dark: black;
  --input-bg: white;         
  --bg-start: #084500;   
  --bg-end: #0B5D00;
  --card-bg: #006756;
  --card-border: #003a30;
  --btn-bg: #bbffb2;
  --btn-hover: #a8e69f;
  --btn-text: #0B5D00;
  --btn-border: rgb(3, 27, 0);
  --btn-shadow: #4a834225;
}

#app {
  height: 100vh;
  padding: 10px;
  box-sizing: border-box;
}

body {
  background: linear-gradient(to bottom right, var(--bg-start), var(--bg-end));
  height: 100vh;
}

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

h1 { 
  color: var(--text-light);
}

.card {
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  border: 2px solid var(--card-border);
  border-radius: 30px;
  margin: 25px;
  background: var(--card-bg);
  color: var(--text-light);
}

input, textarea {
  background: var(--input-bg);
  border: none;
  border-radius: 5px;
  margin: 15px;
  color: var(--text-dark);
  padding: 3px;
}
input:active, textarea:active {
  background: var(--input-bg);
}

.btn {
  background: var(--btn-bg);
  border: 2px solid var(--btn-border);
  color: var(--btn-text);
  box-shadow: 2px 2px 1px 1px var(--btn-shadow);
}

.btn:hover {
  background: var(--btn-hover);
  border: 2px solid var(--btn-border);

}
</style>