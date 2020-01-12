<template>
  <div class="user-profile-div">
    <h1>User Profile</h1>
    <hr />
    <h4 class="mb-5">ID : {{ credential.username }}</h4>
    <h4 class="mb-5">E-mail : {{ credential.email }}</h4>
    <h4 class="mb-5" v-if="credential.gender===false">Gender : Man</h4>
    <h4 class="mb-5" v-else>Gender : Woman</h4>
  </div>
</template>

<script>


export default {
  name: "UserProfileForm",
  props:{
    credential:{
      type: Object,
      require : true
    }
  },
  
  data() {
    return {
    };
  },
};
</script>

<style>
</style>