import { useRouter } from 'next/navigation';
import Image from 'next/image'
import { SignIn } from '@/components/sign-in';

export default function LoginPage() {
  return (
    <>
      <SignIn />
    </>
  );
}