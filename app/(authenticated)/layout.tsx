import Link from 'next/link';
import { Inter } from 'next/font/google'

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
      <body>
        <div class="Header w-[1440px] h-[100px] flex-col justify-center items-start inline-flex">
          <div class="Globalbar w-[1440px] h-[60px] relative">
            <div class="GlobalBar w-[1440px] h-[60px] left-0 top-0 absolute bg-blue-700"></div>
            <div class="GlobalbarEnd w-[715px] h-[55px] left-[722px] top-[2px] absolute">
              <div class="GlobalBarEnd w-[715px] h-[55px] left-0 top-0 absolute bg-white"></div>
              <div class="AppheaderUser w-8 h-8 left-[672px] top-[13px] absolute">
                <div class="ImgUser w-8 h-8 left-0 top-0 absolute bg-zinc-300"></div>
                <img class="ProfilePic2 w-8 h-8 left-0 top-0 absolute" src="../../public/next.svg" />
              </div>
            </div>
            <div class="GlobalbarStart w-[715px] h-[55px] left-[2px] top-[2px] absolute">
              <div class="GlobalBarStart w-[715px] h-[55px] left-0 top-0 absolute bg-white"></div>
              <div class="AppheaderLogo w-8 h-8 left-[13px] top-[13px] absolute">
                <div class="ImgLog w-8 h-8 left-0 top-0 absolute bg-green-500"></div>
                <img class="Compass1 w-8 h-8 left-0 top-0 absolute" src="https://avatars.githubusercontent.com/u/24626409?v=4" alt size="32" height="32" width="32" />
              </div>
            </div>
          </div>
          <div class="LocalBar w-[1440px] h-10 bg-zinc-300"></div>
        </div>
        <hr />
        {children}
      </body>
    </html>
  );
}
