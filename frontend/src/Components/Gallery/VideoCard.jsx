import styled from 'styled-components'
import { useBucket } from '../../Api/useBucket'

const Card = styled.div({
  borderRadus: "5px",
  boxShadow: "0 0 0 2px #ddd",
  padding: "5px",
  width: "50%"
})
export const VideoCard = ({video}) => {
  console.log(video.name)
  const { data } = useBucket({bucket_key: video.name})
  console.log(data)
  return (
    <Card>
      <video width="100%" height="100%" src={ data } controls preload="auto"/>
    </Card>
  )
}