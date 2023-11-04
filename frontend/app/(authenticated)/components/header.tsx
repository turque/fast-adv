import Image from 'next/image'

import { getUserById } from '../users/services/get-user-by-id';
import ProfileImage from './ProfileImage';


function Header() {
  return (
    <header className='grid grid-cols-2 gap-4 bg-gray-100'>
      <div dir="ltr">
        <div className="grid place-items-center h-20 w-20">
          <div className="h-14 w-14 grid place-items-center bg-red-300 rounded-full">
            <Image
              src="/img/compass.svg"
              width={50}
              height={50}
              alt="Picture of the author"
            />
          </div>
        </div>
      </div>

      <div dir="rtl">
        <div className="grid place-items-center h-20 w-20 left-">
          <div className="h-14 w-14 grid place-items-center rounded-full">
            <ProfileImage />
          </div>
        </div>
      </div>
    </header>
  );
}


export default Header
