import Image from 'next/image'

export default function Header() {
    return (
        <div className='bg-slate-300'>
          <div className="flex flex-row bg-green-100">
            <div className="basic-1/2 bg-green-400 object-left">
              <Image
                  src="/api/img/compass.png"
                  width={32}
                  height={32  }
                  alt="Picture of the author"
                />
            <div className="basic-1/2 bg-blue-300">
              <div>
                <Image className='object-right  '
                    src="/api/img/perfil-roxo.png"
                    width={32}
                    height={32  }
                    alt="Picture of the author"
                  />
              </div>
            </div>
            </div>
          </div>
          <div></div>
        </div>
    );
  }
