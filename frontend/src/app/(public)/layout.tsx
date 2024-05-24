import '../globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <section>
      <header></header>
      <nav></nav>
      {children}
    </section>

  )
}
