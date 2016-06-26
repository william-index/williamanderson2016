---
$title@: A Team-based Workflow for Tumblr Theme Development
$slug: teams-for-tumblr-themes
$subtitle: ""
$dates:
  published: 2015/03/22
$excerpt: A proposed workflow for developing a Tumblr theme with a team of developers.
$cover_img: 2015/images/tumblr_themes/cover.gif
$public: true
---
While major brands such as Skittles turn to Tumblr not only for broadcasting their identity, but also as the host for their brand websites, the demand for development of custom themes has increased. From my readings online however, there is little noted about a sane workflow for a team of developers to work together on a single Tumblr theme. The use of just one textfield full of html that represents all layouts proves problematic. There is however a way around it.

<img src="/static/images/blog/tumblr_themes/skittles_com.jpg" class="full" alt='Skittles.com Mar 22, 2015'/>
_\* I was not involved in making the Skittles website, its just an example of the draw and cultural force of Tumblr._

# Assumptions/ pre-reqs/ limits

In this explanation I'll be talking specifically about using [Middleman](http://middlemanapp.com) and ruby-related stack of haml/Sass/coffee. However, these could in theory be substituted for any other build environment or framework. However, experience in some form of environment that allows for concatenating files as well as using some form of source version control system is a must (I'll refer to git throughout the article, but mentally replace that with /whatever/).

**Warning**
*As Tumblr is https, you will either need to find a way to implement https/SSL on your local environment, OR use a browser that will allow you to access an http file from a site with SSL. This is not an issue for the final deploy, but rather for the development environment, as Tumblr is accessed via https. For OSX, Safari will allow you to work like this even over http. If you know of an easy way in general to get this working with Middleman, please (PLEASE) comment below.*

# The Database is your Bottleneck
### Setting up the "server"

Despite my experience working on themes, even with a solid workflow the one bottleneck you are most likely to encounter is the "database."

**Each team member should set up their own private blog for development for the project.**

This means during dev, your content will ALWAYS be out of sync, with each member uploading their own placeholder content. As modifications are made to the DOM (more later) each engineer would be able to update their dev theme at their own discression.

### The DOM bottleneck alternative

If you have a small team, or one member who is normally responsible for creating the DOM/backend while other just skin and add functionality, you MAY want to consider sharing one dev blog between the whole team, and only that engineer in particular having access to the admin. This is also an option to consider if your content is HIGHLY curated and styled/structured a-typically from the average Tumblr blog.

# Building the site

## Directories and Files
Perhaps the greatest/most important element to this workflow is partitioning files into smaller more bite-size chunks. Editing one core theme file between X number of engineers will lead to endless conflicts in your version control system, so a series of includes is key. If you are using Middleman, this will take the form of a series of partials.

So you will end up with some form of file structure like this

[sourcecode:ruby]

source/
  layouts/
    theme.haml
  pages/
    _landing.haml
    _photo.haml
    _photoset.haml
    _quote.haml
    index.haml.html
[/sourcecode]

In the above, the theme.haml is used purely to bring your individual templates together. You can also simplify the number of pages you use to just being \_landing and \_permalink if all your permalink pages are the same. So you may end up with a theme.haml along these lines.

[sourcecode:haml]

!!!
%html
  %head
  %body
    = partial "/pages/landing"
    = partial "/pages/permalink"
[/sourcecode]

## Page Templates

Now you are ready to get started on building the DOM. You can assign tasks to developers or have them choose in whatever your normal management style is (we have a Kanban board) and let individuals work on specific layouts. The theme variables for the blog flow in just like normal plain text, and haml works the same as always. So for each file, you will use the conditional wraps to build the layout.

[sourcecode:haml]

{block:IndexPage}
%section#blogRoll
  {block:Posts}
  %article
    %a{href: "{Permalink}"}
      %h1 Example
  {/block:Posts}
{/block:IndexPage}
[/sourcecode]

This allows for linking about these as separate views for the website or as unique pages. You can get creative with the partials and includes as well, to reduce duplication of overlapping elements and to share templates for certain similar post types.

### Updating the DOM

*This is the most laborious part and the only one not automated, let me know if you think of something better in the comments below.*

When working on the DOM, check your local server and view source. This is like proofreading to make sure its rendering how you want. You'll want to make sure its as desired and do as much work there as possible before each "push" to staging. By push to staging, I mean run a

[sourcecode:bash]

bundle exec middleman build
[/sourcecode]

and then copy and paste the innards of build/index.html into the Tumblr theme editor.

As each dev has their own blog, they will update as needed. As source code is merged their builds will include code from the other engineers.

## Including resources

During dev, any resources used (js/css) should be linked to on your local environment. So in the case of Middleman, most likely to http://localhost:4567/etc.... This way, as you make changes to scripts and styling, they will update in realtime based on the resources that Middleman is compiling in real time.

Breaking out your Sass into partials for sections/whatever will also ease the multi-developer workflow. The same goes for scripts. But there are [numerous articles](http://theSassway.com/beginner/how-to-structure-a-Sass-project) on doing this, so I wont expand upon it here.

*In Middleman, the [Asset Pipeline](https://middlemanapp.com/advanced/asset_pipeline/) makes it easy to split apart the classes of your js/coffee into other files, and also to combine all of your scripts into a single all.js*

So all together your file structure/flow will look something like the below. Where syncing source, will keep everyones scripts and style up to date, but leave them having to move the DOM to their dev blog when needed. Or if using the database bottleneck approach, they wont have to do anything to see changes reflected, but also only one team member (at a time at least) will have the ability to update it.

[![Tumblr team workflow by William Anderson](/static/images/blog/tumblr_themes/tumblr_flow.gif)](images/tumblr_themes/tumblr_flow.gif)

# "Pushing" to "Prod"

Pushing to production isn't bad, but its a bit of a manual process (an easy-ish one, I promise).

If you planned and structured your scripts and styles well, you are hopefully working from just one file for each. This will make things easier. Build your project, and then upload the compiled files to the [Tumblr Static Uploader](https://www.tumblr.com/themes/upload_static_file). This will provide you with URLs to the files on Tumblr's servers, which you can then include in place of the local links in your themes <head>. This should probably be done in a production branch.

After that just copy and paste the build/index.html contents into the theme builder and you should be good to go!

Questions, Suggestions/Etc all welcome below.
