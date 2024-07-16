import React from "react";
import Cards from "@/components/Cards";

export default function Home() {
  const races = [
    {
      id: 1,
      name: "Malacara Chapada Diamantina",
      image: "/img/33_MALACARA_CHAPADA_2025_1.png",
      race_date: "02/05/2025",
      place: "Lençois, BA",
      distance: 500
    },
    {
      id: 2,
      name: "BOA 2024",
      image: "/img/BOA_2024.png",
      race_date: "29/06/2024",
      place: "São João da Aliança, GO",
      distance: 180
    },
    {
      id: 3,
      name: "Malacara Cânios do Sul",
      image: "/img/27_logo_prova_canions_05.png",
      race_date: "05/07/2021",
      place: "Praia Grande, SC",
      distance: 500
    },
    {
      id: 4,
      name: "Haka",
      image: "/img/compass.png",
      race_date: "05/07/2019",
      place: "Praia Grande, SC",
      distance: 300
    },
  ];
  return (
    <div className="gap-2 grid grid-cols-2 sm:grid-cols-4">
      {races.map((item) => (
        <Cards
          key={item.id}
          {...item}
        />
      ))}
    </div>
  );
}
