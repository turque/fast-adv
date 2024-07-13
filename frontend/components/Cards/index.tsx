import React from "react";
import { Card, CardBody, CardFooter, CardHeader, Image } from "@nextui-org/react";
import { RaceInterface } from "@/src/app/(authenticated)/users/models/race";


export default function Cards(race: RaceInterface) {
  return (
    <Card shadow="sm" isPressable>
      <CardHeader>
        <b>{race.name}</b>
      </CardHeader>
      <CardBody className="overflow-visible p-0">
        <Image
          isZoomed
          shadow="sm"
          radius="lg"
          // width="100%"
          alt={race.name}
          className="w-full object-cover h-[140px]"
          src={race.image}
          fallbackSrc="/img/compass.png"
        />
      </CardBody>
      <CardFooter className="text-small justify-between">
        <b className="text-default-500">{race.distance} km</b>
        <p className="text-default-500">{race.race_date}</p>
      </CardFooter>
    </Card>
  );
}

