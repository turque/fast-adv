import Image from 'next/image'
import { getUserById } from '../users/services/get-user-by-id';

const imageStyle = {
  borderRadius: '50%',
  border: '1px solid #fff',
}

interface ProfileImageProps {
  userId: string;
}

export default async function ProfileImage({ userId }: ProfileImageProps) {
    const user = await getUserById(userId);

    return (
      <Image src={user.avatar} width={50} height={50} style={imageStyle} alt="Imagem de perfil" />
    )
}
