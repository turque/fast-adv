import Image from 'next/image'
import { getUserById } from '../users/services/get-user-by-id';

const imageStyle = {
  borderRadius: '50%',
  border: '1px solid #fff',
}

// export default async function ProfileImage({
//     params,
// }: {
//     params: { userId: string };
// }) {
//     const user = await getUserById(params.userId);

//     return <Image src={user.avatar} width={50} height={50} style={imageStyle} />

// }

export default async function ProfileImage() {
  return <Image src="/img/perfil-roxo.png" width={50} height={50} style={imageStyle} alt="Imagem de perfil" />
}
