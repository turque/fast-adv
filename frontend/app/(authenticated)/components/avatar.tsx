import React from "react";
import {Avatar} from "@nextui-org/react";

function UserAvatar() {
  return (
    <div className="flex gap-4 items-center">
      <Avatar src="/img/perfil-roxo.png" className="w-6 h-6 text-tiny"  />
      <Avatar src="/img/perfil-roxo.png" size="md" />
    </div>
  );
}

export default UserAvatar;