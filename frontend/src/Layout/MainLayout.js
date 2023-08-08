import { Helmet } from "react-helmet";

export const MainLayout = (props) => {
  return <>
    <Helmet>
      <title>
        Hockey Vision
      </title>
    </Helmet>

    <div>
      {props.children}
    </div>

  </>
}