<script lang="ts">
    import { Router, Link, Route } from 'svelte-routing';
    import Home from './views/Home.svelte'

    import { applyHttpInterceptors } from './interceptors';

    import { Redirect } from './components';

    import { SignIn, PageNotFound, Users } from './views';

    export let url = '';

    applyHttpInterceptors();

    
</script>

<div class="section columns">
    <Router {url}>
        <nav>
            <Link to="/">Home</Link>
            <Link to="/users">Users</Link>
          </nav>
        <main class="column">
            <Route path="/">
                <Redirect path="/home" />
              </Route>
              <Route path="/home" component={Home} />
              <Route path="/signin" component={SignIn} />
              <Route path="/users" component={Users} />
              <Route component={PageNotFound} />
        </main>
    </Router>
</div>
