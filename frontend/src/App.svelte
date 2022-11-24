<script lang="ts">
    import { Router, Link, Route } from 'svelte-routing';
    import Home from './views/Home.svelte'

    import { applyHttpInterceptors } from './interceptors';

    import { Redirect, SignIn, PageNotFound } from './components';

    export let url = '';

    applyHttpInterceptors();

    
</script>

<div class="section columns">
    <Router {url}>
        <main class="column">
            <Route path="/">
                <Redirect path="/home" />
              </Route>
              <Route path="/home" component={Home} />
              <Route path="/signin" component={SignIn} />
              <Route path="**" component={PageNotFound} />
        </main>
    </Router>
</div>
