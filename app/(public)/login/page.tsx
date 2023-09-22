'use client';

import { useRouter } from 'next/navigation';

export default function LoginPage() {
  const router = useRouter();

  return (
    <form
      onSubmit={(e) => {
        router.push('/');
        e.preventDefault();
      }}
    >
      <div className='bg-red-600'>
        <label>Email:</label>
        <input />
      </div>
      <div>
        <label>Senha:</label>
        <input type="password" />
      </div>
      <div>
        <button type="submit">Entrar</button>
      </div>
    </form>
  );
}