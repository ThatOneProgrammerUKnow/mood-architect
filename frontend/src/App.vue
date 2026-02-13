<!-- JAVASCRIPT -->
<script setup>
import { computed, ref } from 'vue'

const name = ref('')
const feeling = ref('')
const affirmation = ref('')
const loading = ref(false)
const error = ref('')

async function submitForm() {
  error.value = ""
  affirmation.value = ""
  loading.value = true

  // Post data to backend
  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/api/affirmation/`, {
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


<!-- HTML -->
<template>
  <h1>Mood Architect</h1>
  <section>
    <form @submit.prevent="submitForm" class="card">
      <h2>Welcome to Marisa Peers Mood Architect!</h2>

      <label for="name">What is your name?</label>
      <input type="text" id="name" v-model="name">

      <label for="feeling">Describe how you are feeling:</label>
      <textarea rows="5" id="feeling" v-model="feeling"></textarea>

      <button class="btn" type="submit">Generate Response</button>
    </form>

    <div class="card">
      <p v-if="loading">Generating response...</p>
      <p v-else-if="error" class="color-red">{{ error }}</p>
      <p v-else-if="affirmation">{{ affirmation }}</p>
      <p v-else>Response will appear here</p>
    </div>
  </section>
</template>

<!-- CASCADING STYLE SHEETS -->
<style>
:root {
  --text-light: white;
  --text-dark: black;
  --input-bg: rgb(228, 228, 228);         
  --bg: #274c77;   
  --card-bg: #FFFFFF;
  --card-border: #003a30;

  --btn-bg: #a3cef1;
  --btn-hover: #9dc6e7;
  --btn-text: #3e5568;
  --btn-border: #6a8499;
  --btn-shadow: #80a7c725;
}

#app { 
  padding: 10px;
  box-sizing: border-box;
  background: var(--bg);
}

body {
  background: var(--bg);
}

section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;
}

h1 { 
  color: var(--text-light);
}
p {
  font-size: 18px;
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
  color: var(--text-dark);
}

input, textarea {
  background: var(--input-bg);
  border: none;
  border-radius: 5px;
  margin: 15px;
  color: var(--text-dark);
  padding: 5px;
  font-size: 18px;
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

/* Utilities */
.color-red {color:rgb(255, 63, 63);}


@media (max-width: 768px) {
  section {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }

  .card {
    margin: 10px;
    width: auto; /* ensure full width */
  }

  input, textarea {
    width: 100%;
    margin: 10px 0;
  }

  button.btn {
    width: 100%;
  }
}
</style>