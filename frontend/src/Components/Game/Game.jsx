import { Container, Stack } from "@mui/material"
import { usePlaceholder } from "../../Api/usePlaceholder"
import { useRequest } from "../../Api/useRequest"
import { GAME_URL } from "../../constants"
import { useParams } from "react-router-dom"
import { VideoPlayer } from "./VideoPlayer"
import { ClusterDisplay } from "./ClusterDisplay"

export const Game = () => {
  const {id: gameid} = useParams()
  const {data: gamedata, placeholder1} = usePlaceholder(useRequest({route: `${GAME_URL}${gameid}`}))
  const title = gamedata?.title

  return (
    <div>
      <h5>{title}</h5>
      { !!placeholder1
        ? placeholder1
        : (
          <Container>
            <Stack spacing={5}>
              { !!gamedata && gamedata.videos.map((video, index) =>
                <div key={index}>
                  <VideoPlayer video={video}/>
                  <div className="clusterdisp">
                    <ClusterDisplay video={video}/>
                  </div>
                </div>
              )}
            </Stack>
          </Container>
        )}

    </div>
  )
}