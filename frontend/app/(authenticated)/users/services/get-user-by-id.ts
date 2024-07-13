import { User } from '../models/user';

// export function getUserById(id: Promise<User>){
//   return new Promise<User>((resolve, reject) => {
//     const user = users[id];
//     if (user) {
//       resolve(user);
//     } else {
//       reject(`User with id ${id} not found`);
//     }
//   });
// }

export async function getUserById(userId: Promise<User> ){

  try {
    const response = await fetch(`https://reqres.in/api/users/${userId}`);
  
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const user = await response.json();
    return user.data as User;
  } catch (error) {
    console.error('There has been a problem with your fetch operation:', error);
  }
}