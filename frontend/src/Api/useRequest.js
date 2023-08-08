import axios from 'axios';
import { API_URL } from '../constants';
import { useEffect, useState } from 'react';

export const useRequest = ({
  route,
  method="GET",
  responseType="json",
  data,
  params={},
  skip=false
}) => {
  
  const [state, setState] = useState({
    data: undefined,
    loading: !skip,
    error: undefined,
    fetched: false
  })

  const fetchData = () => {
    setState({...state, loading: true})
    axios({
      method,
      url: `${route}`,
      responseType,
      data,
      params
    }).then(res => {
      setState({...state, data: res.data, loading: false, fetched: true})
    }).catch(err => {
      console.error(err)
      setState({...state, error: err, loading: false})
    })
  }

  useEffect(() => {
    if (!skip && !state.fetched) {
      fetchData()
    }
  }, [skip])

  return state
}