import { GetObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import { useEffect, useState } from "react";

export const useBucket = ({
  bucket_key,
  skip=false
}) => {
  const [state, setState] = useState({
    data: undefined,
    loading: !skip,
    error: undefined,
    fetched: false
  })
  const createPresignedUrlWithClient = ({ region, bucket, key }) => {
    const client = new S3Client({
      region: region,
      credentials: {
        accessKeyId: process.env.REACT_APP_AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.REACT_APP_AWS_SECRET_ACCESS_KEY
      }})
    const command = new GetObjectCommand({
      Bucket: bucket,
      Key: key,
      mode: 'no-cors',
      ResponseContentType: `video/mp4`
    });
    return getSignedUrl(client, command, { expiresIn: 3600 });
  };
  const getVideo = async () => {
    setState({...state, loading: true})
    try {
      const clientUrl = await createPresignedUrlWithClient({
        region: 'us-east-1',
        bucket: "hockeyvision-videos",
        key: `${bucket_key}`,
      });
      console.log(clientUrl)
      setState({...state, data: clientUrl, loading: false, fetched: true})
    } catch (err) {
      console.error(err);
      setState({...state, error: err, loading: false})
    }
  };

  useEffect(() => {
    if (!skip && !state.fetched) {
      getVideo()
    }
  }, [skip])

  return state
}