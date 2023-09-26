import Image from 'next/image'

import { getUserById } from '../users/services/get-user-by-id';
import ProfileImage from './ProfileImage';

function Header() {
    return (
        <div>
          <div className="bg-green-100">
          <div className="relative h-10 w-10">
            <div className="absolute right-0 w-8">
              <Image
                  src="/api/img/compass.png"
                  width={32}
                  height={32  }
                  alt="Picture of the author"
                />
            </div>
          </div>

            <div className="absolute inset-y-0 right-0 w-14">
                <Image
                    src="/api/img/perfil-roxo.png"
                    width={32}
                    height={32}
                    alt="Picture of the author"
                  />
            </div>
          </div>
        </div>
    );
  }


function Header2() {
  return (
    <div className='grid grid-cols-2 gap-4 bg-gray-100'>
      <div dir="ltr">
        <div className="grid place-items-center h-20 w-20 bg-red-100">
          {/* <div className="h-14 w-14 grid place-items-center bg-red-300 rounded-full"> */}
          <Image
              src="/img/compass.png"
              width={50}
              height={50}
              alt="Picture of the author"
            />
          {/* </div> */}
        </div>
      </div>
    
      <div dir="rtl">
        <div className="grid place-items-center h-20 w-20 bg-blue-100 left-">
          <div className="h-14 w-14 grid place-items-center bg-blue-300 rounded-full">
            <ProfileImage params='https://reqres.in/img/faces/4-image.jpg' />
            
          </div>
        </div>
      </div>
    </div>
  );
}


  export default Header2
