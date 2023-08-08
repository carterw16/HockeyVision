import { usePlaceholder } from "../../Api/usePlaceholder"
import { useRequest } from "../../Api/useRequest"
import { VideoCard } from "./VideoCard"
import { Container, Stack } from '@mui/material'
import { VIDEO_URL } from "../../constants"

export const Gallery = ({}) => {
  const {data, placeholder} = usePlaceholder(useRequest({route: VIDEO_URL}))
  // console.log(data)
  // console.log(placeholder)
  return (
    <div>
      <h5>Gallery</h5>
      { !!placeholder ? placeholder : null}
      <Container>
        <Stack spacing={5}>
          { !!data && data.map((video, index) => <VideoCard video={video} key={index}/>)}
        </Stack>
      </Container>
    </div>
  )
}