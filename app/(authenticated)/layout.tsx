import { Inter } from 'next/font/google'

import Header from './components/header'

import '../globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Sistema Minha Aventura!',
  description: 'Sistema de organização de time de corridad e aventura',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className='bg-slate-200'>
        <Header />
        <hr />
        {children}
      </body>
    </html>
  );
}
