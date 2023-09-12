import { useBucket } from '../../Api/useBucket'
import { CroppedVideo } from './CroppedVideo';


export const ClusterDisplay= ({video}) => {
  const { data } = useBucket({bucket_key: video.name})
  return (
    <div className='clusters'>
    {!!video && video.clusters.map((cluster, index1) => {
      return <div key={index1} className='cluster'>
        <h1>Person {index1+1}</h1>
        {!!cluster && cluster.pred_tracks.map((track, index2) => {
          return <div key={index2}>
            <CroppedVideo track={track}
              video={data}
              fps={video.fps}
              srcWidth={video.width}
              srcHeight={video.height}/>
          </div>
        })}
        </div>
    })}
    </div>
  )
}