import styled from 'styled-components'
import { useBucket } from '../../Api/useBucket'

const Card = styled.div({
  borderRadus: "5px",
  boxShadow: "0 0 0 2px #ddd",
  padding: "5px",
  width: "50%",
  marginLeft: "auto",
  marginRight: "auto"
})
export const VideoPlayer = ({video}) => {
  const { data } = useBucket({bucket_key: video.name})

  const handleVideoMounted = element => {
  };
  return (
    <Card>
      <video
        width="100%"
        height="100%"
        ref = {handleVideoMounted}
        src={ data }
        controls
        preload="auto"/>
    </Card>
  )
}