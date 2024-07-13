import { Providers } from './providers'

export const metadata = {
    title: 'Minha Corrida de Aventura!',
    description: 'Gestão de time e provas de corrida de aventura',
}


export default function RootLayout({children}: {children: React.ReactNode}) {
    return (
        <html lang="en" className='ligth'>
        <body>
          <Providers>
            {children}
          </Providers>
        </body>
      </html>
    )
}