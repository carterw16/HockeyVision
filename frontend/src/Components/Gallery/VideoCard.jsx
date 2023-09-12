import styled from 'styled-components'
import { useBucket } from '../../Api/useBucket'

const Card = styled.div({
  borderRadus: "5px",
  boxShadow: "0 0 0 2px #ddd",
  padding: "5px",
  width: "50%"
})
export const VideoCard = ({video}) => {
  const { data } = useBucket({bucket_key: video.name})
  return (
    <Card>
      <video width="100%" height="100%" src={ data } controls={false} preload="auto"/>
    </Card>
  )
}