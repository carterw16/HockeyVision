import { usePlaceholder } from "../../Api/usePlaceholder"
import { useRequest } from "../../Api/useRequest"
import { VideoCard } from "./VideoCard"
import { Container, Stack } from '@mui/material'
import { VIDEO_URL } from "../../constants"
import { useNavigate } from "react-router-dom"

export const Gallery = () => {
  const {data, placeholder} = usePlaceholder(useRequest({route: VIDEO_URL}))
  const navigate = useNavigate()
  return (
    <div>
      <h1>Gallery</h1>
      { !!placeholder ? placeholder : null}
      <Container>
        <Stack spacing={5}>
          { !!data && data.map((video, index) =>
            <div key={index} onClick={(e) => navigate(`../game/${video.game}`)}>
              <VideoCard video={video}/>
            </div>
          )}
        </Stack>
      </Container>
    </div>
  )
}