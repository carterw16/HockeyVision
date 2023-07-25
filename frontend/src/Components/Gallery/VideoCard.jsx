import styled from 'styled-components'

const Card = styled.div({
  borderRadus: "5px",
  boxShadow: "0 0 0 2px #ddd",
  padding: "5px"
})
export const VideoCard = ({video}) => {
  return (
    <Card>
      { video.name }
    </Card>
  )
}