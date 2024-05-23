import { User } from '../models/user';

const users = {
  1: {
    "id": 1,
    "email": "george.bluth@reqres.in",
    "first_name": "George",
    "last_name": "Bluth",
    "avatar": "/img/perfil-roxo.png",
    // "avatar": "https://reqres.in/img/faces/1-image.jpg"
  },
  2: {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
  },
  3: {
    "id": 3,
    "email": "emma.wong@reqres.in",
    "first_name": "Emma",
    "last_name": "Wong",
    "avatar": "https://reqres.in/img/faces/3-image.jpg"
  },
  4: {
    "id": 4,
    "email": "eve.holt@reqres.in",
    "first_name": "Eve",
    "last_name": "Holt",
    "avatar": "https://reqres.in/img/faces/4-image.jpg"
  },
  5: {
    "id": 5,
    "email": "charles.morris@reqres.in",
    "first_name": "Charles",
    "last_name": "Morris",
    "avatar": "https://reqres.in/img/faces/5-image.jpg"
  },
  6: {
    "id": 6,
    "email": "tracey.ramos@reqres.in",
    "first_name": "Tracey",
    "last_name": "Ramos",
    "avatar": "https://reqres.in/img/faces/6-image.jpg"
    }

}

export function getUserById(id: Promise<User>){
  return new Promise<User>((resolve, reject) => {
    const user = users[id];
    if (user) {
      resolve(user);
    } else {
      reject(`User with id ${id} not found`);
    }
  });
}

// export async function getUserById(userId: Promise<User> ){

//   try {
//     const response = await fetch(`https://reqres.in/api/users/${userId}`);
  
//     if (!response.ok) {
//       throw new Error('Network response was not ok');
//     }
//     const user = await response.json();
//     return user.data as User;
//   } catch (error) {
//     console.error('There has been a problem with your fetch operation:', error);
//   }
// }