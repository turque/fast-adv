export interface RaceInterface {
    id: number;
    name: string;
    place: string;
    race_date: string;
    distance: number; 
    url_race?: string;
    race_description?: string;
    place_description?: string;
    observations?: string;
    image?: string;
  };