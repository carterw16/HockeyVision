// const srcfps = 28.30753869196206
// const vidWidth = 1620
// const vidHeight = 1080
export const CroppedVideo = ({
  video,
  track,
  // Pixels passed in as integers
  size=.5,
  srcHeight,
  srcWidth,
  fps,
  videoPct=0.5
  }) => {
    const height = srcHeight * size
    const width = srcWidth * size
    const startFrame = track.lifetime[0]
    const end = track.lifetime[1]
    const selectedFrame = parseInt((end-startFrame)*videoPct)
    const selectedBbox = track.bboxes[selectedFrame]
    const startTime = (startFrame + selectedFrame) / fps

    const offsetLeft = - (selectedBbox[0] / srcWidth) * width
    const offsetTop = - (selectedBbox[1] / srcHeight) * height

    const handleVideoMounted = element => {
      if (element !== null) {
        element.currentTime = startTime;
      }
    };

    const convertCoordinates = (srcPixels) => {
      const x = (srcPixels[0] / srcWidth) * width
      const y = (srcPixels[1] / srcHeight) * height
      return [x,y]
    }

    const getBboxDims = (bbox) => {
      const width = bbox[2] - bbox[0]
      const height = bbox[3] - bbox[1]
      return convertCoordinates([width, height])
    }

    return (
      <div style={{
        padding: "5%",
        width: getBboxDims(selectedBbox)[0],
        height: getBboxDims(selectedBbox)[1],
        overflow: "hidden",
        display: "block",
        margin: "auto",
      }}>
        <video
          width={width}
          height={height}
          ref = {handleVideoMounted}
          src={ video }
          preload="auto"
          style={{
            marginLeft: offsetLeft,
            marginTop: offsetTop
          }}/>
      </div>
    )
}