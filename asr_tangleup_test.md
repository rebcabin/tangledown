# This is a First Test of the Emergency Tangleup System


## .lein-failures

<!-- #raw -->
<noweb name=".lein-failures_085450">
<!-- #endraw -->

```
{"asr.core-test" ["a-test"]}```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/.lein-failures">
<!-- #endraw -->

```
<block name=".lein-failures_085450"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## project.clj

<!-- #raw -->
<noweb name="project_53FFF1">
<!-- #endraw -->

```clojure id=a9341f3e-5c07-4023-a2dc-458ea75a01df
(defproject asr "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.11.1"]
                 [org.clojure/core.logic "1.0.1"]
                 [org.clojure/test.check "1.1.1"]
                 [instaparse "1.4.12"]
                 [swiss-arrows "0.6.0"]
                 [camel-snake-kebab "0.4.3"]
                 [compliment/compliment "0.3.9"]]
  :main ^:skip-aot asr.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all
                       :jvm-opts ["-Dclojure.compiler.direct-linking=true"]}})






























































```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/project.clj">
<!-- #endraw -->

```clojure id=a9341f3e-5c07-4023-a2dc-458ea75a01df
<block name="project_53FFF1"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## LICENSE

<!-- #raw -->
<noweb name="LICENSE_EFDAFA">
<!-- #endraw -->

```
Eclipse Public License - v 2.0

    THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
    PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
    OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.

1. DEFINITIONS

"Contribution" means:

  a) in the case of the initial Contributor, the initial content
     Distributed under this Agreement, and

  b) in the case of each subsequent Contributor:
     i) changes to the Program, and
     ii) additions to the Program;
  where such changes and/or additions to the Program originate from
  and are Distributed by that particular Contributor. A Contribution
  "originates" from a Contributor if it was added to the Program by
  such Contributor itself or anyone acting on such Contributor's behalf.
  Contributions do not include changes or additions to the Program that
  are not Modified Works.

"Contributor" means any person or entity that Distributes the Program.

"Licensed Patents" mean patent claims licensable by a Contributor which
are necessarily infringed by the use or sale of its Contribution alone
or when combined with the Program.

"Program" means the Contributions Distributed in accordance with this
Agreement.

"Recipient" means anyone who receives the Program under this Agreement
or any Secondary License (as applicable), including Contributors.

"Derivative Works" shall mean any work, whether in Source Code or other
form, that is based on (or derived from) the Program and for which the
editorial revisions, annotations, elaborations, or other modifications
represent, as a whole, an original work of authorship.

"Modified Works" shall mean any work in Source Code or other form that
results from an addition to, deletion from, or modification of the
contents of the Program, including, for purposes of clarity any new file
in Source Code form that contains any contents of the Program. Modified
Works shall not include works that contain only declarations,
interfaces, types, classes, structures, or files of the Program solely
in each case in order to link to, bind by name, or subclass the Program
or Modified Works thereof.

"Distribute" means the acts of a) distributing or b) making available
in any manner that enables the transfer of a copy.

"Source Code" means the form of a Program preferred for making
modifications, including but not limited to software source code,
documentation source, and configuration files.

"Secondary License" means either the GNU General Public License,
Version 2.0, or any later versions of that license, including any
exceptions or additional permissions as identified by the initial
Contributor.

2. GRANT OF RIGHTS

  a) Subject to the terms of this Agreement, each Contributor hereby
  grants Recipient a non-exclusive, worldwide, royalty-free copyright
  license to reproduce, prepare Derivative Works of, publicly display,
  publicly perform, Distribute and sublicense the Contribution of such
  Contributor, if any, and such Derivative Works.

  b) Subject to the terms of this Agreement, each Contributor hereby
  grants Recipient a non-exclusive, worldwide, royalty-free patent
  license under Licensed Patents to make, use, sell, offer to sell,
  import and otherwise transfer the Contribution of such Contributor,
  if any, in Source Code or other form. This patent license shall
  apply to the combination of the Contribution and the Program if, at
  the time the Contribution is added by the Contributor, such addition
  of the Contribution causes such combination to be covered by the
  Licensed Patents. The patent license shall not apply to any other
  combinations which include the Contribution. No hardware per se is
  licensed hereunder.

  c) Recipient understands that although each Contributor grants the
  licenses to its Contributions set forth herein, no assurances are
  provided by any Contributor that the Program does not infringe the
  patent or other intellectual property rights of any other entity.
  Each Contributor disclaims any liability to Recipient for claims
  brought by any other entity based on infringement of intellectual
  property rights or otherwise. As a condition to exercising the
  rights and licenses granted hereunder, each Recipient hereby
  assumes sole responsibility to secure any other intellectual
  property rights needed, if any. For example, if a third party
  patent license is required to allow Recipient to Distribute the
  Program, it is Recipient's responsibility to acquire that license
  before distributing the Program.

  d) Each Contributor represents that to its knowledge it has
  sufficient copyright rights in its Contribution, if any, to grant
  the copyright license set forth in this Agreement.

  e) Notwithstanding the terms of any Secondary License, no
  Contributor makes additional grants to any Recipient (other than
  those set forth in this Agreement) as a result of such Recipient's
  receipt of the Program under the terms of a Secondary License
  (if permitted under the terms of Section 3).

3. REQUIREMENTS

3.1 If a Contributor Distributes the Program in any form, then:

  a) the Program must also be made available as Source Code, in
  accordance with section 3.2, and the Contributor must accompany
  the Program with a statement that the Source Code for the Program
  is available under this Agreement, and informs Recipients how to
  obtain it in a reasonable manner on or through a medium customarily
  used for software exchange; and

  b) the Contributor may Distribute the Program under a license
  different than this Agreement, provided that such license:
     i) effectively disclaims on behalf of all other Contributors all
     warranties and conditions, express and implied, including
     warranties or conditions of title and non-infringement, and
     implied warranties or conditions of merchantability and fitness
     for a particular purpose;

     ii) effectively excludes on behalf of all other Contributors all
     liability for damages, including direct, indirect, special,
     incidental and consequential damages, such as lost profits;

     iii) does not attempt to limit or alter the recipients' rights
     in the Source Code under section 3.2; and

     iv) requires any subsequent distribution of the Program by any
     party to be under a license that satisfies the requirements
     of this section 3.

3.2 When the Program is Distributed as Source Code:

  a) it must be made available under this Agreement, or if the
  Program (i) is combined with other material in a separate file or
  files made available under a Secondary License, and (ii) the initial
  Contributor attached to the Source Code the notice described in
  Exhibit A of this Agreement, then the Program may be made available
  under the terms of such Secondary Licenses, and

  b) a copy of this Agreement must be included with each copy of
  the Program.

3.3 Contributors may not remove or alter any copyright, patent,
trademark, attribution notices, disclaimers of warranty, or limitations
of liability ("notices") contained within the Program from any copy of
the Program which they Distribute, provided that Contributors may add
their own appropriate notices.

4. COMMERCIAL DISTRIBUTION

Commercial distributors of software may accept certain responsibilities
with respect to end users, business partners and the like. While this
license is intended to facilitate the commercial use of the Program,
the Contributor who includes the Program in a commercial product
offering should do so in a manner which does not create potential
liability for other Contributors. Therefore, if a Contributor includes
the Program in a commercial product offering, such Contributor
("Commercial Contributor") hereby agrees to defend and indemnify every
other Contributor ("Indemnified Contributor") against any losses,
damages and costs (collectively "Losses") arising from claims, lawsuits
and other legal actions brought by a third party against the Indemnified
Contributor to the extent caused by the acts or omissions of such
Commercial Contributor in connection with its distribution of the Program
in a commercial product offering. The obligations in this section do not
apply to any claims or Losses relating to any actual or alleged
intellectual property infringement. In order to qualify, an Indemnified
Contributor must: a) promptly notify the Commercial Contributor in
writing of such claim, and b) allow the Commercial Contributor to control,
and cooperate with the Commercial Contributor in, the defense and any
related settlement negotiations. The Indemnified Contributor may
participate in any such claim at its own expense.

For example, a Contributor might include the Program in a commercial
product offering, Product X. That Contributor is then a Commercial
Contributor. If that Commercial Contributor then makes performance
claims, or offers warranties related to Product X, those performance
claims and warranties are such Commercial Contributor's responsibility
alone. Under this section, the Commercial Contributor would have to
defend claims against the other Contributors related to those performance
claims and warranties, and if a court requires any other Contributor to
pay any damages as a result, the Commercial Contributor must pay
those damages.

5. NO WARRANTY

EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT
PERMITTED BY APPLICABLE LAW, THE PROGRAM IS PROVIDED ON AN "AS IS"
BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR
IMPLIED INCLUDING, WITHOUT LIMITATION, ANY WARRANTIES OR CONDITIONS OF
TITLE, NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR
PURPOSE. Each Recipient is solely responsible for determining the
appropriateness of using and distributing the Program and assumes all
risks associated with its exercise of rights under this Agreement,
including but not limited to the risks and costs of program errors,
compliance with applicable laws, damage to or loss of data, programs
or equipment, and unavailability or interruption of operations.

6. DISCLAIMER OF LIABILITY

EXCEPT AS EXPRESSLY SET FORTH IN THIS AGREEMENT, AND TO THE EXTENT
PERMITTED BY APPLICABLE LAW, NEITHER RECIPIENT NOR ANY CONTRIBUTORS
SHALL HAVE ANY LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING WITHOUT LIMITATION LOST
PROFITS), HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OR DISTRIBUTION OF THE PROGRAM OR THE
EXERCISE OF ANY RIGHTS GRANTED HEREUNDER, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

7. GENERAL

If any provision of this Agreement is invalid or unenforceable under
applicable law, it shall not affect the validity or enforceability of
the remainder of the terms of this Agreement, and without further
action by the parties hereto, such provision shall be reformed to the
minimum extent necessary to make such provision valid and enforceable.

If Recipient institutes patent litigation against any entity
(including a cross-claim or counterclaim in a lawsuit) alleging that the
Program itself (excluding combinations of the Program with other software
or hardware) infringes such Recipient's patent(s), then such Recipient's
rights granted under Section 2(b) shall terminate as of the date such
litigation is filed.

All Recipient's rights under this Agreement shall terminate if it
fails to comply with any of the material terms or conditions of this
Agreement and does not cure such failure in a reasonable period of
time after becoming aware of such noncompliance. If all Recipient's
rights under this Agreement terminate, Recipient agrees to cease use
and distribution of the Program as soon as reasonably practicable.
However, Recipient's obligations under this Agreement and any licenses
granted by Recipient relating to the Program shall continue and survive.

Everyone is permitted to copy and distribute copies of this Agreement,
but in order to avoid inconsistency the Agreement is copyrighted and
may only be modified in the following manner. The Agreement Steward
reserves the right to publish new versions (including revisions) of
this Agreement from time to time. No one other than the Agreement
Steward has the right to modify this Agreement. The Eclipse Foundation
is the initial Agreement Steward. The Eclipse Foundation may assign the
responsibility to serve as the Agreement Steward to a suitable separate
entity. Each new version of the Agreement will be given a distinguishing
version number. The Program (including Contributions) may always be
Distributed subject to the version of the Agreement under which it was
received. In addition, after a new version of the Agreement is published,
Contributor may elect to Distribute the Program (including its
Contributions) under the new version.

Except as expressly stated in Sections 2(a) and 2(b) above, Recipient
receives no rights or licenses to the intellectual property of any
Contributor under this Agreement, whether expressly, by implication,
estoppel or otherwise. All rights in the Program not expressly granted
under this Agreement are reserved. Nothing in this Agreement is intended
to be enforceable by any entity that is not a Contributor or Recipient.
No third-party beneficiary rights are created under this Agreement.

Exhibit A - Form of Secondary Licenses Notice

"This Source Code may also be made available under the following
Secondary Licenses when the conditions for such availability set forth
in the Eclipse Public License, v. 2.0 are satisfied: GNU General Public
License as published by the Free Software Foundation, either version 2
of the License, or (at your option) any later version, with the GNU
Classpath Exception which is available at
https://www.gnu.org/software/classpath/license.html."

  Simply including a copy of this Agreement, including this Exhibit A
  is not sufficient to license the Source Code under Secondary Licenses.

  If it is not possible or desirable to put the notice in a particular
  file, then You may include the notice in a location (such as a LICENSE
  file in a relevant directory) where a recipient would be likely to
  look for such a notice.

  You may add additional accurate notices of copyright ownership.














































































```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/LICENSE">
<!-- #endraw -->

```
<block name="LICENSE_EFDAFA"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## core_test.clj

<!-- #raw -->
<noweb name="core_test_FEC9CA">
<!-- #endraw -->

```clojure id=2b6c7b96-af88-4d97-92d7-f6818e4ed349
(ns asr.core-test
  (:require [clojure.test :refer :all]
            [asr.core :refer :all]))

(deftest a-test
  (testing "FIXME, I fail."
    (is (= 0 1))))














































































```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/test/asr/core_test.clj">
<!-- #endraw -->

```clojure id=2b6c7b96-af88-4d97-92d7-f6818e4ed349
<block name="core_test_FEC9CA"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## CHANGELOG.md

<!-- #raw -->
<noweb name="CHANGELOG_EE0942">
<!-- #endraw -->

    # Change Log
    All notable changes to this project will be documented in this file. This change log follows the conventions of [keepachangelog.com](http://keepachangelog.com/).
    
    ## [Unreleased]
    ### Changed
    - Add a new arity to `make-widget-async` to provide a different widget shape.
    
    ## [0.1.1] - 2022-09-18
    ### Changed
    - Documentation on how to make the widgets.
    
    ### Removed
    - `make-widget-sync` - we're all async, all the time.
    
    ### Fixed
    - Fixed widget maker to keep working when daylight savings switches over.
    
    ## 0.1.0 - 2022-09-18
    ### Added
    - Files from the new template.
    - Widget maker public API - `make-widget-sync`.
    
    [Unreleased]: https://sourcehost.site/your-name/asr/compare/0.1.1...HEAD
    [0.1.1]: https://sourcehost.site/your-name/asr/compare/0.1.0...0.1.1
    
    ## quoting test
    
    ```clojure
    (-> foo bar baz qux)
    ```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/CHANGELOG.md">
<!-- #endraw -->

```markdown
<block name="CHANGELOG_EE0942"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## pom.properties

<!-- #raw -->
<noweb name="pom_FB70F6">
<!-- #endraw -->

```
artifactId=asr
groupId=asr
version=0.1.0-SNAPSHOT
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/target/default+test+test/classes/META-INF/maven/asr/asr/pom.properties">
<!-- #endraw -->

```
<block name="pom_FB70F6"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## leiningen.core.classpath.extract-native-dependencies

<!-- #raw -->
<noweb name="leiningen.core.classpath_236BC7">
<!-- #endraw -->

```
[{:dependencies {org.clojure/clojure {:vsn "1.11.1", :native-prefix nil}, org.nrepl/incomplete {:vsn "0.1.0", :native-prefix nil}, org.clojure/core.specs.alpha {:vsn "0.2.62", :native-prefix nil}, compliment {:vsn "0.3.9", :native-prefix nil}, org.clojure/spec.alpha {:vsn "0.3.218", :native-prefix nil}, swiss-arrows {:vsn "0.6.0", :native-prefix nil}, camel-snake-kebab {:vsn "0.4.3", :native-prefix nil}, org.clojure/core.logic {:vsn "1.0.1", :native-prefix nil}, instaparse {:vsn "1.4.12", :native-prefix nil}, nrepl {:vsn "0.9.0", :native-prefix nil}, org.clojure/test.check {:vsn "1.1.1", :native-prefix nil}}, :native-path "target/default+test+test/native"} {:native-path "target/default+test+test/native", :dependencies {org.clojure/clojure {:vsn "1.11.1", :native-prefix nil, :native? false}, org.nrepl/incomplete {:vsn "0.1.0", :native-prefix nil, :native? false}, org.clojure/core.specs.alpha {:vsn "0.2.62", :native-prefix nil, :native? false}, compliment {:vsn "0.3.9", :native-prefix nil, :native? false}, org.clojure/spec.alpha {:vsn "0.3.218", :native-prefix nil, :native? false}, swiss-arrows {:vsn "0.6.0", :native-prefix nil, :native? false}, camel-snake-kebab {:vsn "0.4.3", :native-prefix nil, :native? false}, org.clojure/core.logic {:vsn "1.0.1", :native-prefix nil, :native? false}, instaparse {:vsn "1.4.12", :native-prefix nil, :native? false}, nrepl {:vsn "0.9.0", :native-prefix nil, :native? false}, org.clojure/test.check {:vsn "1.1.1", :native-prefix nil, :native? false}}}]```






























































```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/target/default+test+test/stale/leiningen.core.classpath.extract-native-dependencies">
<!-- #endraw -->

```
<block name="leiningen.core.classpath_236BC7"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## pom.properties

<!-- #raw -->
<noweb name="pom_8D3457">
<!-- #endraw -->

```
artifactId=asr
groupId=asr
version=0.1.0-SNAPSHOT
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/target/default/classes/META-INF/maven/asr/asr/pom.properties">
<!-- #endraw -->

```
<block name="pom_8D3457"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## leiningen.core.classpath.extract-native-dependencies

<!-- #raw -->
<noweb name="leiningen.core.classpath_E9962D">
<!-- #endraw -->

```
[{:dependencies {org.clojure/clojure {:vsn "1.11.1", :native-prefix nil}, org.nrepl/incomplete {:vsn "0.1.0", :native-prefix nil}, org.clojure/core.specs.alpha {:vsn "0.2.62", :native-prefix nil}, compliment {:vsn "0.3.9", :native-prefix nil}, org.clojure/spec.alpha {:vsn "0.3.218", :native-prefix nil}, swiss-arrows {:vsn "0.6.0", :native-prefix nil}, camel-snake-kebab {:vsn "0.4.3", :native-prefix nil}, org.clojure/core.logic {:vsn "1.0.1", :native-prefix nil}, instaparse {:vsn "1.4.12", :native-prefix nil}, nrepl {:vsn "0.9.0", :native-prefix nil}, org.clojure/test.check {:vsn "1.1.1", :native-prefix nil}}, :native-path "target/default/native"} {:native-path "target/default/native", :dependencies {org.clojure/clojure {:vsn "1.11.1", :native-prefix nil, :native? false}, org.nrepl/incomplete {:vsn "0.1.0", :native-prefix nil, :native? false}, org.clojure/core.specs.alpha {:vsn "0.2.62", :native-prefix nil, :native? false}, compliment {:vsn "0.3.9", :native-prefix nil, :native? false}, org.clojure/spec.alpha {:vsn "0.3.218", :native-prefix nil, :native? false}, swiss-arrows {:vsn "0.6.0", :native-prefix nil, :native? false}, camel-snake-kebab {:vsn "0.4.3", :native-prefix nil, :native? false}, org.clojure/core.logic {:vsn "1.0.1", :native-prefix nil, :native? false}, instaparse {:vsn "1.4.12", :native-prefix nil, :native? false}, nrepl {:vsn "0.9.0", :native-prefix nil, :native? false}, org.clojure/test.check {:vsn "1.1.1", :native-prefix nil, :native? false}}}]```






























































```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/target/default/stale/leiningen.core.classpath.extract-native-dependencies">
<!-- #endraw -->

```
<block name="leiningen.core.classpath_E9962D"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## repl-port

<!-- #raw -->
<noweb name="repl-port_6A15EC">
<!-- #endraw -->

```
63331```






























































```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/target/default/repl-port">
<!-- #endraw -->

```
<block name="repl-port_6A15EC"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## .hgignore

<!-- #raw -->
<noweb name=".hgignore_14DA39">
<!-- #endraw -->

```
<block name=".hgignore_F91F1E"></block>


```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/.hgignore">
<!-- #endraw -->

```
<block name=".hgignore_14DA39"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## README.md

<!-- #raw -->
<noweb name="README_78018C">
<!-- #endraw -->

    # asr
    
    FIXME: description
    
    ## Installation
    
    Download from http://example.com/FIXME.
    
    ## Usage
    
    FIXME: explanation
    
        $ java -jar asr-0.1.0-standalone.jar [args]
    
    ## Options
    
    FIXME: listing of options this app accepts.
    
    ## Examples
    
    ...
    
    ### Bugs
    
    ...
    
    ### Any Other Sections
    ### That You Think
    ### Might be Useful
    
    ## License
    
    Copyright © 2022 FIXME
    
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License 2.0 which is available at
    http://www.eclipse.org/legal/epl-2.0.
    
    This Source Code may also be made available under the following Secondary
    Licenses when the conditions for such availability set forth in the Eclipse
    Public License, v. 2.0 are satisfied: GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or (at your
    option) any later version, with the GNU Classpath Exception which is available
    at https://www.gnu.org/software/classpath/license.html.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/README.md">
<!-- #endraw -->

```markdown
<block name="README_78018C"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## .gitignore

<!-- #raw -->
<noweb name=".gitignore_07E745">
<!-- #endraw -->

```
<block name=".gitignore_5042DC"></block>


```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/.gitignore">
<!-- #endraw -->

```
<block name=".gitignore_07E745"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## intro.md

<!-- #raw -->
<noweb name="intro_C98463">
<!-- #endraw -->

    # Introduction to asr
    
    TODO: write [great documentation](http://jacobian.org/writing/what-to-write/)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/doc/intro.md">
<!-- #endraw -->

```markdown
<block name="intro_C98463"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## core.clj

<!-- #raw -->
<noweb name="core_F5F43B">
<!-- #endraw -->

```clojure id=11ba9d25-2ad6-4df8-b614-eab51105837e
(ns asr.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))














































































```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/asr/src/asr/core.clj">
<!-- #endraw -->

```clojure id=11ba9d25-2ad6-4df8-b614-eab51105837e
<block name="core_F5F43B"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## genetically-engineered-asr.nextjournal-checkpoint.md

<!-- #raw -->
<noweb name="genetically-engineered-asr.nextjournal-checkpoint_05BF0E">
<!-- #endraw -->

    # Genetically Engineered ASR
    
    Let's generate bits of ASR for testing purposes. Eventually, we'll evolve a big population of generated ASR, with "fitness" measuring "tendency to find bugs."
    
    We'll need a `clojure.spec` for `test.check` to generate ASR instances. Let's generate the `clojure.spec` from the ASDL spec [https://github.com/lcompilers/lpython/blob/84a073ce44a9a74213a4ac5648ee783bd38fc90f/src/libasr/ASR.asdl](https://github.com/lcompilers/lpython/blob/84a073ce44a9a74213a4ac5648ee783bd38fc90f/src/libasr/ASR.asdl#L87-L90) 
    
    # Mechanics
    
    Transition to Tangledown and Tangleup, 18 Sept 2022. This notebook now takes over 1 minute to boot up. I am going to experiment with a literate notebook. Caveats: clojure kernel does NOT work in jupyter lab, so TangleUp will be necessary to maintain the notebook. First step: export this as markdown. Here goes! See you back here later after my experiments!
    
    # Prelude
    
    ## Dependencies
    
    We include *core.logic* for experimentation. `Instaparse` is for parsing. Swiss arrows are just fun. `Camel-snake-kebab` is for naming conventions. `compliment` is for autocompletion in the notebook. 
    
    ```edn no-exec id=ffcf0396-b3f9-40e6-a0c2-654401879781
    {:deps {org.clojure/clojure {:mvn/version "1.11.1"}
            org.clojure/core.logic {:mvn/version "1.0.1"}
            org.clojure/test.check {:mvn/version "1.1.1"}
            instaparse {:mvn/version "1.4.12"}
            swiss-arrows {:mvn/version "0.6.0"}
            camel-snake-kebab {:mvn/version "0.4.3"}
            ;; compliment is for autocompletion in the notebook
            ;; add your libs here (and restart the runtime to pick up changes)
            compliment/compliment {:mvn/version "0.3.9"} } }
    ```
    
    ## Imports
    
    We'll get started in the `user` namespace, just poking around.
    
    ```clojure id=af906587-480d-4f71-855c-e803e5cba1d5
    (require '[clojure.spec.alpha :as s])
    (require '[clojure.pprint])
    (def pp clojure.pprint/pprint)
    (require '[instaparse.core :as insta])
    (require '[clojure.zip :as zip])
    ```
    
    # Motivating Example ASR
    
    Here is an example datum, a tree of ASR from  <https://raw.githubusercontent.com/lcompilers/lpython/main/tests/reference/asr-expr_01-211000e.stdout>. The syntax of this datum is *almost* Clojure: we must move colons from the backs of keys to the fronts. Clojure won't even *read* a symbol followed by a colon, but Clojure interprets a colon followed by a symbol as a Clojure keyword. Those are really convenient. Amongst other things, they're lookup functions in hashmaps.
    
    I'll move the colons by hand, aided by <https://regex101.com/r/kUW4Ug/1>. TODO: with instaparse.
    
    ## ASR for expr_01.py:
    
    Cut and paste, after moving the colons from back to front. It's too long to look at in the notebook, but ...
    
    ```clojure id=9be7df63-a594-451e-bc67-495cf6c8b55d
    (def expr-01-211000 '(TranslationUnit (SymbolTable 1 {:_lpython_main_program (Function (SymbolTable 4 {}) _lpython_main_program [] [] [(SubroutineCall 1 main0 () [] ())] () Source Public Implementation () .false. .false. .false. .false.),:main0 (Function (SymbolTable 2 {:x (Variable 2 x Local () () Default (Integer 4 []) Source Public Required .false.),:x2 (Variable 2 x2 Local () () Default (Integer 8 []) Source Public Required .false.),:y (Variable 2 y Local () () Default (Real 4 []) Source Public Required .false.),:y2 (Variable 2 y2 Local () () Default (Real 8 []) Source Public Required .false.)}) main0 [] [] [(= (Var 2 x) (IntegerBinOp (IntegerBinOp (IntegerConstant 2 (Integer 4 [])) Add (IntegerConstant 3 (Integer 4 [])) (Integer 4 []) (IntegerConstant 5 (Integer 4 []))) Mul (IntegerConstant 5 (Integer 4 [])) (Integer 4 []) (IntegerConstant 25 (Integer 4 []))) ()) (Print () [(Var 2 x)] () ())] () Source Public Implementation () .false. .false. .false. .false.),:main_program (Program (SymbolTable 3 {}) main_program [] [(SubroutineCall 1 _lpython_main_program () [] ())])}) []))
    ```
    
    [result][nextjournal#output#9be7df63-a594-451e-bc67-495cf6c8b55d#result]
    
    Click the tiny right triangle above to see what's in the list. Or, pretty-print it:
    
    ```clojure id=17507f3b-6ac2-47d1-91e3-260161097282
    (pp expr-01-211000)
    ```
    
    By the way, here is the Python that generates the ASR above, from <https://github.com/lcompilers/lpython/blob/84a073ce44a9a74213a4ac5648ee783bd38fc90f/tests/expr_01.py>.
    
    ```python id=f1020f8e-d252-4b90-b78a-e74a366b580e
    def main0():
        x: i32
        x2: i64
        y: f32
        y2: f64
        x = (2+3)*5
        print(x)
    
    main0()
    ```
    
    ## Does the Example Conform to Spec?
    
    *expr-01-211000* is a Clojure Persistent List:
    
    ```clojure id=db3884f0-fd65-4f9d-9341-918c9e4733cd
    (type expr-01-211000)
    ```
    
    [result][nextjournal#output#db3884f0-fd65-4f9d-9341-918c9e4733cd#result]
    
    Write a spec that tests that fact and smoke-test the clojure.spec library:
    
    ```clojure id=cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f
    (s/conform list? expr-01-211000)
    ```
    
    [result][nextjournal#output#cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f#result]
    
    ## Namespace Imports
    
    Once we enter the `asr` namespace via `(ns asr)`, we must again import things we're going to use. We must qualify the expression `expr-01-211000` by the *user* namespace like this: `user/expr-01-211000`; `expr-01-211000` is not in `asr`, it's in `user`.
    
    We can only name clojure.specs with namespaced keywords like `::foo` or `:asr/bar` (<https://blog.jeaye.com/2017/10/31/clojure-keywords/>). 
    
    ```clojure id=60ca7c24-976f-45e5-921f-311004fb1ff4
    (ns asr) ;; enter the namespace implicitly
    (require '[clojure.spec.alpha :as s])
    (require '[clojure.pprint])
    (def pp clojure.pprint/pprint)
    (defn echo [x] (pp x) x)  ;; TODO: macro?
    (require '[instaparse.core :as insta])
    (require '[clojure.zip :as zip])
    (require '[camel-snake-kebab.core :as csk])
    (require '[clojure.spec.gen.alpha :as gen])
    (require '[clojure.spec.test.alpha :as stest])
    (require '[clojure.test.check.generators :as tgen])
    ```
    
    ### Kebab'bed Namespaced Keywords for Specs from Symbols in ASR
    
    Transform conventional names in ASR PascalCase to conventional namespaced keywords in kebab-case in clojure.spec. It works on symbols or on strings. We can write a spec for this function, too? Specs all the way down!
    
    ```clojure id=db8dcc66-f14b-4344-9205-9c3f9ab20ee6
    (defn nskw-kebab-from  ;; TODO: macro?
      [sym-or-string]  
      (keyword "asr" (name (csk/->kebab-case sym-or-string)))
      ;; Found by experiment that ->> doesn't work, here.
      #_(->> sym csk/->kebab-case #(keyword "asr" %)) )
    (s/fdef nskw-kebab-from
      :args (s/alt :str string? :sym symbol?)
      :ret keyword?)
    (stest/instrument `nskw-kebab-from)
    
    (nskw-kebab-from 'TranslationUnit)
    (nskw-kebab-from "TranslationUnit")
    ;(nskw-kebab-from 42)
    ```
    
    # A Grammar for ASDL Specs
    
    ## ASDL Spec for ASR
    
    Here is a big string that contains the ASR.asdl, the spec that any ASR instance must conform to. I had to escape the double-quote marks by hand.
    
    ```clojure id=14995343-d18f-4579-b61f-96398c72c557
    (def all-asr "-- Abstract Semantic Representation (ASR) definition
    
    -- The aim of ASR is to represent all semantics in a non-redundant way, and that
    -- has all the semantic information available locally, so that the backend can
    -- do a single pass over ASR and have all the information at hand to generate
    -- code.
    --
    -- ASR is always semantically valid Fortran code. It is as far from the original
    -- Fortran language code as possible (i.e. everything is explicitly figured out,
    -- all semantic information gathered and readily available locally from each ASR
    -- node), while ensuring no semantic information was lost (no lowering was
    -- done), so one can still generate Fortran code from ASR that will be logically
    -- equivalent to the original code.
    --
    -- ASR can be used to do Fortran level transformations (such as optimizations).
    
    -- ASDL's builtin types are:
    --   * identifier
    --   * int (signed integers of infinite precision)
    --   * string
    -- We extend these by:
    --   * bool (.true. / .false.)
    --   * float (floating point number of infinite precision)
    --   * symbol_table (scoped Symbol Table implementation)
    --   * node (any ASR node)
    --
    -- Note: `symbol_table` contains `identifier` -> `symbol` mappings.
    
    module ASR {
    
    unit
        = TranslationUnit(symbol_table global_scope, node* items)
    
    -- # Documentation for the symbol type
    
    -- Each symbol has either `symtab` (local symbol table) or `parent_symtab`
    -- (where this symbol is stored). One can get to parent_symtab via symtab, so
    -- only one is present.
    
    -- Each symbol has a `name` for easy lookup of the name of the symbol when only
    -- having a pointer to it.
    
    -- abi=Source means the symbol's implementation is included (full ASR),
    -- otherwise it is external (interface ASR, such as procedure interface).
    
    -- SubroutineCall/FunctionCall store the actual final resolved subroutine or
    -- function (`name` member). They also store the original symbol
    -- (`original_name`), which can be one of: null, GenericProcedure or
    -- ExternalSymbol.
    
    -- When a module is compiled, it is parsed into full ASR, an object file is
    -- produced, the full ASR (abi=Source, \" body\" is non-empty) is transformed into
    -- interface ASR (abi=LFortran, \"body\" is empty). Both interface and full ASR
    -- is saved into the mod file.
    
    -- When a module is used, it is first looked up in the symbol table (as either
    -- full or interface ASR) and used if it is present. Otherwise a mod file is
    -- found on the disk, loaded (as either full or interface ASR for LFortran's
    -- mod file, depending on LFortran's compiler options; or for GFortran's mod
    -- file the corresponding interface ASR is constructed with abi=GFortran) and
    -- used. After the ASR is loaded, the symbols that are used are represented as
    -- ExternalSymbols in the current scope of the symbol table.
    
    -- ExternalSymbol represents symbols that cannot be looked up in the current
    -- scoped symbol table. As an example, if a variable is defined in a module,
    -- but used in a nested subroutine, that is not an external symbol
    -- because it can be resolved in the current symbol table (nested subroutine)
    -- by following the parents. However if a symbol is used from a different
    -- module, then it is an external symbol, because usual symbol resolution by
    -- going to the parents will not find the definition. The `module_name` member
    -- is the name of the module the symbol is in, the `scope_names` is a list of
    -- names if the symbol is in a nested symbol table. For example if it is a
    -- local variable in a function `f` that is nested in function `g`, then
    -- `scope_names=[g, f]`.
    
    -- REPL: each cell is parsed into full ASR, compiled + executed, the full ASR
    -- is transformed into interface ASR (abi=LFortran) and kept in the symbol
    -- table. A new cell starts with an empty symbol table, whose parent symbol
    -- table is the previous cell. That allows function / declaration shadowing.
    
    
    symbol
        = Program(symbol_table symtab, identifier name, identifier* dependencies,
            stmt* body)
        | Module(symbol_table symtab, identifier name, identifier* dependencies,
            bool loaded_from_mod, bool intrinsic)
        | Function(symbol_table symtab, identifier name, expr* args,
            ttype* type_params, stmt* body, expr? return_var, abi abi,
            access access, deftype deftype, string? bindc_name, bool elemental,
            bool pure, bool module, bool inline)
        | GenericProcedure(symbol_table parent_symtab, identifier name,
            symbol* procs, access access)
        | CustomOperator(symbol_table parent_symtab, identifier name,
            symbol* procs, access access)
        | ExternalSymbol(symbol_table parent_symtab, identifier name,
            symbol external, identifier module_name, identifier* scope_names,
            identifier original_name, access access)
        | DerivedType(symbol_table symtab, identifier name, identifier* members,
            abi abi, access access, symbol? parent)
        | EnumType(symbol_table symtab, identifier name, identifier* members,
            abi abi, access access, ttype type, symbol? parent)
        | Variable(symbol_table parent_symtab, identifier name, intent intent,
            expr? symbolic_value, expr? value, storage_type storage, ttype type,
            abi abi, access access, presence presence, bool value_attr)
        | ClassType(symbol_table symtab, identifier name, abi abi, access access)
        | ClassProcedure(symbol_table parent_symtab, identifier name, identifier
            proc_name, symbol proc, abi abi)
        | AssociateBlock(symbol_table symtab, identifier name, stmt* body)
        | Block(symbol_table symtab, identifier name, stmt* body)
    
    storage_type = Default | Save | Parameter | Allocatable
    access = Public | Private
    intent = Local | In | Out | InOut | ReturnVar | Unspecified
    deftype = Implementation | Interface
    presence = Required | Optional
    
    -- # Documentation for the ABI type
    
    -- External Yes: the symbol's implementation is not part of ASR, the
    -- symbol is just an interface (e.g., subroutine/function interface, or variable
    -- marked as external, not allocated by this ASR).
    
    -- External No:  the symbol's implementation is part of ASR (e.g.,
    -- subroutine/function body is included, variables must be allocated).
    
    -- abi=Source: The symbol's implementation is included in ASR, the backend is
    -- free to use any ABI it wants (it might also decide to inline or eliminate
    -- the code in optimizations).
    
    -- abi=LFortranModule/GFortranModule/BindC: the symbol's implementation is
    -- stored as machine code in some object file that needs to be linked in. It
    -- uses the specified ABI (one of LFortran module, GFortran module or C ABI).
    -- An interface that uses `iso_c_binding` and `bind(c)` is represented using
    -- abi=BindC.
    
    -- abi=Interactive: the symbol's implementation has been provided by the
    -- previous REPL execution (e.g., if LLVM backend is used for the interactive
    -- mode, the previous execution generated machine code for this symbol's
    -- implementation that was loaded into memory). Note: this option might be
    -- converted/eliminated to just use LFortran ABI in the future.
    
    -- abi=Intrinsic: the symbol's implementation is implicitly provided by the
    -- language itself as an intrinsic function. That means the backend is free to
    -- implement it in any way it wants. The function does not have a body, it is
    -- just an interface.
    
    abi                   -- External     ABI
        = Source          --   No         Unspecified
        | LFortranModule  --   Yes        LFortran
        | GFortranModule  --   Yes        GFortran
        | BindC           --   Yes        C
        | Interactive     --   Yes        Unspecified
        | Intrinsic       --   Yes        Unspecified
    
    
    stmt
        = Allocate(alloc_arg* args, expr? stat, expr? errmsg, expr? source)
        | Assign(int label, identifier variable)
        | Assignment(expr target, expr value, stmt? overloaded)
        | Associate(expr target, expr value)
        | Cycle()
        -- deallocates if allocated otherwise throws a runtime error
        | ExplicitDeallocate(symbol* vars)
        -- deallocates if allocated otherwise does nothing
        | ImplicitDeallocate(symbol* vars)
        | DoConcurrentLoop(do_loop_head head, stmt* body)
        | DoLoop(do_loop_head head, stmt* body)
        | ErrorStop(expr? code)
        | Exit()
        | ForAllSingle(do_loop_head head, stmt assign_stmt)
            -- GoTo points to a GoToTarget with the corresponding target_id within
            -- the same procedure. We currently use `int` IDs to link GoTo with
            -- GoToTarget to avoid issues with serialization.
        | GoTo(int target_id)
            -- An empty statement, a target of zero or more GoTo statements
            -- the `id` is only unique within a procedure
        | GoToTarget(int id)
        | If(expr test, stmt* body, stmt* orelse)
        | IfArithmetic(expr test, int lt_label, int eq_label, int gt_label)
        | Print(expr? fmt, expr* values, expr? separator, expr? end)
        | FileOpen(int label, expr? newunit, expr? filename, expr? status)
        | FileClose(int label, expr? unit, expr? iostat, expr? iomsg, expr? err, expr? status)
        | FileRead(int label, expr? unit, expr? fmt, expr? iomsg, expr? iostat, expr? id, expr* values)
        | FileRewind(int label, expr? unit, expr? iostat, expr? err)
        | FileInquire(int label, expr? unit, expr? file, expr? iostat, expr? err,
                  expr? exist, expr? opened, expr? number, expr? named,
                  expr? name, expr? access, expr? sequential, expr? direct,
                  expr? form, expr? formatted, expr? unformatted, expr? recl,
                  expr? nextrec, expr? blank, expr? position, expr? action,
                  expr? read, expr? write, expr? readwrite, expr? delim,
                  expr? pad, expr? flen, expr? blocksize, expr? convert,
                  expr? carriagecontrol, expr? iolength)
        | FileWrite(int label, expr? unit, expr? fmt, expr? iomsg, expr? iostat, expr? id, expr* values, expr? separator, expr? end)
        | Return()
        | Select(expr test, case_stmt* body, stmt* default)
        | Stop(expr? code)
        | Assert(expr test, expr? msg)
        | SubroutineCall(symbol name, symbol? original_name, call_arg* args, expr? dt)
        | Where(expr test, stmt* body, stmt* orelse)
        | WhileLoop(expr test, stmt* body)
        | Nullify(symbol* vars)
        | Flush(int label, expr unit, expr? err, expr? iomsg, expr? iostat)
        | ListAppend(expr a, expr ele)
        | AssociateBlockCall(symbol m)
        | CPtrToPointer(expr cptr, expr ptr, expr? shape)
        | BlockCall(int label, symbol m)
        | SetInsert(expr a, expr ele)
        | SetRemove(expr a, expr ele)
        | ListInsert(expr a, expr pos, expr ele)
        | ListRemove(expr a, expr ele)
        | ListClear(expr a)
        | DictInsert(expr a, expr key, expr value)
    
    
    expr
        = IfExp(expr test, expr body, expr orelse, ttype type, expr? value)
            -- Such as: (x, y+z), (3.0, 2.0) generally not known at compile time
        | ComplexConstructor(expr re, expr im, ttype type, expr? value)
        | NamedExpr(expr target, expr value, ttype type)
        | FunctionCall(symbol name, symbol? original_name,
                call_arg* args, ttype type, expr? value, expr? dt)
        | DerivedTypeConstructor(symbol dt_sym, expr* args, ttype type, expr? value)
        | EnumTypeConstructor(symbol dt_sym, expr* args, ttype type, expr? value)
        | ImpliedDoLoop(expr* values, expr var, expr start, expr end,
                        expr? increment, ttype type, expr? value)
        | IntegerConstant(int n, ttype type)
        | IntegerBOZ(int v, integerboz intboz_type, ttype? type)
        | IntegerBitNot(expr arg, ttype type, expr? value)
        | IntegerUnaryMinus(expr arg, ttype type, expr? value)
        | IntegerCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | IntegerBinOp(expr left, binop op, expr right, ttype type, expr? value)
        | RealConstant(float r, ttype type)
        | RealUnaryMinus(expr arg, ttype type, expr? value)
        | RealCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | RealBinOp(expr left, binop op, expr right, ttype type, expr? value)
        | ComplexConstant(float re, float im, ttype type)
        | ComplexUnaryMinus(expr arg, ttype type, expr? value)
        | ComplexCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | ComplexBinOp(expr left, binop op, expr right, ttype type, expr? value)
        | LogicalConstant(bool value, ttype type)
        | LogicalNot(expr arg, ttype type, expr? value)
        | LogicalCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | LogicalBinOp(expr left, logicalbinop op, expr right, ttype type, expr? value)
        | TemplateBinOp(expr left, binop op, expr right, ttype type, expr? value)
    
        | ListConstant(expr* args, ttype type)
        | ListLen(expr arg, ttype type, expr? value)
        | ListConcat(expr left, expr right, ttype type, expr? value)
    
        | SetConstant(expr* elements, ttype type)
        | SetLen(expr arg, ttype type, expr? value)
    
        | TupleConstant(expr* elements, ttype type)
        | TupleLen(expr arg, ttype type, expr value)
    
        | StringConstant(string s, ttype type)
        | StringConcat(expr left, expr right, ttype type, expr? value)
        | StringRepeat(expr left, expr right, ttype type, expr? value)
        | StringLen(expr arg, ttype type, expr? value)
        | StringItem(expr arg, expr idx, ttype type, expr? value)
        | StringSection(expr arg, expr? start, expr? end, expr? step, ttype type, expr? value)
        | StringCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | StringOrd(expr arg, ttype type, expr? value)
        | StringChr(expr arg, ttype type, expr? value)
    
        | DictConstant(expr* keys, expr* values, ttype type)
        | DictLen(expr arg, ttype type, expr? value)
    
        | Var(symbol v)
    
        | ArrayConstant(expr* args, ttype type)
        | ArrayItem(expr v, array_index* args, ttype type, expr? value)
        | ArraySection(expr v, array_index* args, ttype type, expr? value)
        | ArraySize(expr v, expr? dim, ttype type, expr? value)
        | ArrayBound(expr v, expr? dim, ttype type, arraybound bound,
                     expr? value)
        | ArrayTranspose(expr matrix, ttype type, expr? value)
        | ArrayMatMul(expr matrix_a, expr matrix_b, ttype type, expr? value)
        | ArrayPack(expr array, expr mask, expr? vector, ttype type, expr? value)
        | ArrayReshape(expr array, expr shape, ttype type, expr? value)
    
        | BitCast(expr source, expr mold, expr? size, ttype type, expr? value)
        | DerivedRef(expr v, symbol m, ttype type, expr? value)
        | EnumRef(symbol v, symbol? m, string property, ttype type, expr? value)
        | OverloadedCompare(expr left, cmpop op, expr right, ttype type, expr? value, expr overloaded)
        | OverloadedBinOp(expr left, binop op, expr right, ttype type, expr? value, expr overloaded)
        | Cast(expr arg, cast_kind kind, ttype type, expr? value)
        | ComplexRe(expr arg, ttype type, expr? value)
        | ComplexIm(expr arg, ttype type, expr? value)
        | DictItem(expr a, expr key, expr? default, ttype type, expr? value)
        | CLoc(expr arg, ttype type, expr? value)
        | PointerToCPtr(expr arg, ttype type, expr? value)
        | GetPointer(expr arg, ttype type, expr? value)
        | ListItem(expr a, expr pos, ttype type, expr? value)
        | TupleItem(expr a, expr pos, ttype type, expr? value)
        | ListSection(expr a, array_index section, ttype type, expr? value)
        | ListPop(expr a, expr? index, ttype type, expr? value)
        | DictPop(expr a, expr key, ttype type, expr? value)
        | SetPop(expr a, ttype type, expr? value)
        | IntegerBitLen(expr a, ttype type, expr? value)
    
    
    -- `len` in Character:
    -- >=0 ... the length of the string, known at compile time
    --  -1 ... character(*), i.e., inferred at runtime
    --  -2 ... character(:), allocatable (possibly we might use -1 for that also)
    --  -3 ... character(n+3), i.e., a runtime expression stored in `len_expr`
    
    -- kind: The `kind` member selects the kind of a given type. We currently
    -- support the following:
    -- Integer kinds: 1 (i8), 2 (i16), 4 (i32), 8 (i64)
    -- Real kinds: 4 (f32), 8 (f64)
    -- Complex kinds: 4 (c32), 8 (c64)
    -- Character kinds: 1 (utf8 string)
    -- Logical kinds: 1, 2, 4: (boolean represented by 1, 2, 4 bytes; the default
    --     kind is 4, just like the default integer kind, consistent with Python
    --     and Fortran: in Python \"Booleans in Python are implemented as a subclass
    --     of integers\", in Fortran the \"default logical kind has the same storage
    --     size as the default integer\"; we currently use kind=4 as default
    --     integer, so we also use kind=4 for the default logical.)
    
    ttype
        = Integer(int kind, dimension* dims)
        | Real(int kind, dimension* dims)
        | Complex(int kind, dimension* dims)
        | Character(int kind, int len, expr? len_expr, dimension* dims)
        | Logical(int kind, dimension* dims)
        | Set(ttype type)
        | List(ttype type)
        | Tuple(ttype* type)
        | Derived(symbol derived_type, dimension* dims)
        | Enum(symbol enum_type, dimension *dims)
        | Class(symbol class_type, dimension* dims)
        | Dict(ttype key_type, ttype value_type)
        | Pointer(ttype type)
        | CPtr()
        | TypeParameter(identifier param, dimension* dims, restriction* rt)
    
    restriction = Restriction(trait rt)
    
    trait = SupportsZero | SupportsPlus | Divisible | Any
    
    binop = Add | Sub | Mul | Div | Pow | BitAnd | BitOr | BitXor | BitLShift | BitRShift
    
    logicalbinop = And | Or | Xor | NEqv | Eqv
    
    cmpop = Eq | NotEq | Lt | LtE | Gt | GtE
    
    integerboz = Binary | Hex | Octal
    
    arraybound = LBound | UBound
    
    cast_kind
        = RealToInteger
        | IntegerToReal
        | LogicalToReal
        | RealToReal
        | TemplateToReal
        | IntegerToInteger
        | RealToComplex
        | IntegerToComplex
        | IntegerToLogical
        | RealToLogical
        | CharacterToLogical
        | CharacterToInteger
        | CharacterToList
        | ComplexToLogical
        | ComplexToComplex
        | ComplexToReal
        | LogicalToInteger
        | RealToCharacter
        | IntegerToCharacter
        | LogicalToCharacter
    
    dimension = (expr? start, expr? length)
    
    alloc_arg = (symbol a, dimension* dims)
    
    attribute = Attribute(identifier name, attribute_arg *args)
    
    attribute_arg = (identifier arg)
    
    call_arg = (expr? value)
    
    tbind = Bind(string lang, string name)
    
    array_index = (expr? left, expr? right, expr? step)
    
    do_loop_head = (expr? v, expr? start, expr? end, expr? increment)
    
    case_stmt = CaseStmt(expr* test, stmt* body) | CaseStmt_Range(expr? start, expr? end, stmt* body)
    
    }")
    ```
    
    [result][nextjournal#output#14995343-d18f-4579-b61f-96398c72c557#result]
    
    ## Instaparse Grammar for ASDL
    
    We'll parse the ASDL spec for ASR into Clojure vectors and hashmaps, then generate clojure.specs for terms and forms from the vectors and hashmaps.
    
    The only thing less-than-obvious in the following grammar are angle brackets. They mean "don't bother reporting this term." Cuts down on clutter in the output.
    
    The grammar says:
    
    1. An ASDL spec is a bunch of ***productions*** or ASDL-DEFs
    2. An ASDL-DEF, aka ***speclet***, is a triple of (a) ***term*** or ASDL-TERM, (b) an equals sign, and (c) one or more ASDL-FORMs separated by vertical bar characters. The meaning of an ASDL-DEF is an *alternation*, a list of alternative ASDL-FORMs. 
    3. There are three *kinds* of ASDL-FORM or speclet: a ***composite***, a ***symconst***, or a ***tuple***. 
    4. A *composite* is a ASDL-HEAD ***head*** followed by ASDL-ARGSs args. Args are identical in shape to a tuple. 
    5. A *symconst* is just an identifier, reckoned as the *head* of the symconst. 
    6. A tuple is a comma-separated list (in round brackets) of pairs of ***type*** and ***variable***.
    
        A tuple is anonymous, but we gensym a *head* for them, so that every kind of ASDL-FORM has a head, for convenience.
    7. Types can have *quantitative qualifiers*, aka *multiplicities*: STAR or QUES, meaning that the variable denotes "zero or more" and "at least one" instance of the type respectively. The default quantity is "exactly once."
    
    The big picture to remember about *terms* and *heads* is that a *speclet* looks like one of the following three:
    
    1. `term` `=` `composite-`*`head`*`-1` `args` `|` `composite-`*`head`*`-2` `args` `|` ...
    2. `term` `=` `symconst-`*`head`* `|` `symconst-`*`head`* `|` ...
    3. `term` `=` `tuple` (anonymous \[gensymmed\] *head*) 
    
    A *term* corresponds to one or more (a *bunch* of) *heads*, but each head corresponds to exactly one term. 
    
    A term has exactly one *speclet*. The speclet is the whole line, left-hand side (term) and right-hand side (bunch of *forms*, one per head). 
    
    All forms in a speclet have the same kind, composite, symconst, or tuple. There won't be a mixture of coposites and speclets, for instance, on the right-hand side of any term.
    
    In addition to the 3 kinds, it turns out there are (at one count) 28 terms and speclets, and 227 heads, forms, and clojure.specs when we're done. The number grows slowly as we add features to AS.
    
    ```clojure id=029fe8f0-78f1-4cf8-8271-807e090e83a4
    (def asdl-grammar "
       MODULE         = SPC* <'module'> SPC* IDENT LBRACE SPEC RBRACE
       SPEC           = (ASDL-DEF SPC*)*
    (* **************************************************************** *)
      <SPC>           = <#'\\s*(--[^\\n]*)?'> (* eat comments quickly * *)
      <BAR>           = <SPC* '|' SPC*>
      <COMMA>         = <SPC* ',' SPC*>
       STAR           = <SPC* '*' SPC*>
       QUES           = <SPC* '?' SPC*>
      <EQ>            = <SPC* '=' SPC*>
      <LBRACE>        = <SPC* '{' SPC*>
      <RBRACE>        = <SPC* '}' SPC*>
      <LPAR>          = <SPC* '(' SPC*>
      <RPAR>          = <SPC* ')' SPC*>
      <IDENT>         = #'[A-Za-z_][A-Za-z0-9_\\.\\-]*'
    (* **************************************************************** *)
       ASDL-DEF       = ASDL-TERM EQ ASDL-FORMS  (* aka 'speclet' ***** *)
       ASDL-TERM      = IDENT
       ASDL-FORMS     = ASDL-FORM (BAR ASDL-FORM)*
      <ASDL-FORM>     = ASDL-COMPOSITE
                      | ASDL-SYMCONST
                      | ASDL-TUPLE
      
       ASDL-COMPOSITE = ASDL-HEAD ASDL-ARGS
       ASDL-SYMCONST  = IDENT
       ASDL-TUPLE     = ASDL-ARGS
    
       ASDL-HEAD      = IDENT
       ASDL-ARGS      = LPAR ASDL-DECL (COMMA ASDL-DECL)* RPAR
                      | LPAR RPAR
       ASDL-DECL      = ASDL-TYPE SPC* ASDL-NYM
       ASDL-TYPE      = IDENT | IDENT STAR | IDENT QUES
       ASDL-NYM       = IDENT
      ")
    (def asdl-parser (insta/parser asdl-grammar))
    nil  ;; Stanch big output.
    ```
    
    Capture the parse of ASR.asdl into hiccup format **(**<https://github.com/weavejester/hiccup>**).** 
    
    ```clojure id=28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d
    (def asr-pre-spec (asdl-parser all-asr))
    ```
    
    [result][nextjournal#output#28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d#result]
    
    ## Raw Hiccup for all Speclets
    
    Strip off the `module` info, leaving only ASDL-DEFs, i.e., *speclets*. 
    
    ```clojure id=ef06350e-bcee-4e53-ac1f-d9975ed18fc6
    (def speclets
      (vec (rest
             ((-> (zip/vector-zip asr-pre-spec)
                zip/down zip/right zip/right) 0))))
    ```
    
    [result][nextjournal#output#ef06350e-bcee-4e53-ac1f-d9975ed18fc6#result]
    
    ## Hashmap from Speclet
    
    This isn't literate programming, so I can't show you "what we're doing" before I show you "how we do it." But at least I can *tell* you "what we're doing:" we need a function to produce a Clojure hash-map from any speclet, i.e., any ASDL-DEF: its ASDL-TERM and all its ASDL-FORMs
    
    ## Helpers
    
    ### Shallow Hashmap from Speclet
    
    Step 1: Convert the top level of one speclet to a hashmap:
    
    ```clojure id=0a784b7a-e707-41fa-8598-d4a4586c77c6
    (defn shallow-map-from-speclet
      "Convert an ASDL-DEF into a map from :ASDL-TERM to the name of 
      the speclet and from :ASDL-FORMS into a list of alternative forms."
      [speclet]
      (let [[sign asdl-term asdl-forms] speclet
            _ (assert (= sign :ASDL-DEF))  ;; TODO: replace with s/fspec
            [sign & forms] asdl-forms  ;; listify forms
            _ (assert (= sign :ASDL-FORMS))
            renested [asdl-term [:ASDL-FORMS forms]]
            denested (mapcat identity renested)]
        (apply hash-map denested)))
    (pp (shallow-map-from-speclet (speclets 3)))  ;; symconst unit test
    (pp (shallow-map-from-speclet (speclets 0)))  ;; composite unit test
    (pp (shallow-map-from-speclet (speclets 22))) ;; tuple unit tes
    ```
    
    ### Decl Hashmap
    
    Step 2: Convert a single ASDL-DECL, which is either the right-hand side of an ASDL-TUPLE or the argument list of an ASDL-COMPOSITE, into a hashmap:
    
    ```clojure id=4fb2c34f-9857-4ec8-bdea-f6776d3093c1
    (defn decl-map
        "Convert [:ASDL-DECL [:ASDL-TYPE ...] [:ASDL-NYM ...]]
        into {:ASDL-TYPE ..., :MULTIPLICITY ..., :ASDL-NYM ...}.
        TODO: Rewrite argument validation with s/fdef."
        [decl-hiccup]
        (let [_ (assert (= (decl-hiccup 0) :ASDL-DECL))
              [sign type-nym & opt] (decl-hiccup 1)
              _ (assert (= sign :ASDL-TYPE))
              [sign decl-nym] (decl-hiccup 2)
              _ (assert (= sign :ASDL-NYM))]
          {:ASDL-TYPE type-nym
           :MULTIPLICITY (case opt
                           (([:STAR])) ::zero-or-more
                           (([:QUES])) ::at-most-once
                           ::once)  ;; default
           :ASDL-NYM decl-nym}))
    ```
    
    ### ASDL Form
    
    Step 3: Convert each of the three kinds of ASDL-FORM --- symconsts, composites, and tuples --- to a hashmap.
    
    All tuples get a unique, gensymmed namespaced-keyword name for a *head*.
    
    ```clojure id=6a635fa0-719a-4eb6-9698-1ed0488244f7
    (defmulti asdl-form first)
    (defmethod asdl-form :ASDL-SYMCONST [form]
      (apply hash-map form))
    (defmethod asdl-form :ASDL-COMPOSITE [form]
      (let [[_ head args-pre] form
            [_ & decls] args-pre]  ;; & means listify
        {:ASDL-COMPOSITE {:ASDL-HEAD (second head)
                          :ASDL-ARGS (map decl-map decls)}}))
    (defmethod asdl-form :ASDL-TUPLE [form]
      (let [[_ args-pre] form
            [_ & decls] args-pre] ;; & means listify
        {:ASDL-TUPLE (name (gensym "asr-tuple"))
         :ASDL-ARGS (map decl-map decls)}))
    ;;; unit test
    (pp (->> (shallow-map-from-speclet (speclets 22))
          :ASDL-FORMS
          (map asdl-form)))
    ```
    
    ## Hashmap from Speclet, Itself
    
    One entire speclet to a hashmap:
    
    ```clojure id=711cc44d-616c-4d69-a01e-5138898ee4e2
    (defn hashmap-from-speclet [speclet]
      (let [pre (shallow-map-from-speclet speclet)
            term (:ASDL-TERM pre)
            forms (map asdl-form (:ASDL-FORMS pre))]
        {:ASDL-TERM term
         :ASDL-FORMS forms}))
    (pp (hashmap-from-speclet (speclets 0)))  
    (pp (hashmap-from-speclet (speclets 3)))
    (pp (hashmap-from-speclet (speclets 22)))
    ```
    
    # Big Map of Speclets From Terms
    
    Example: term `::symbol` maps to `::Function`, `::Program`, `::Module`, and more.
    
    Except for `SymbolTable`, which is not written, terms are in `snake_case`.
    
    Have fun clicking around the large output of this cell. There are about 28 terms with about 227 heads.
    
    ```clojure id=68960eae-8344-4331-a419-cea794ee5480
    (defn map-pair-from-speclet-map [speclet-map]
      [(keyword "asr" (:ASDL-TERM speclet-map))  ;; no kebab'bing
       (:ASDL-FORMS speclet-map)])
    (def big-map-of-speclets-from-terms
      ;; TODO: Make some nice swiss arrows to do all this.
      (apply hash-map
        (mapcat identity  ;; flatten one level
          (map
            (comp map-pair-from-speclet-map
              hashmap-from-speclet)
            speclets))))
    ```
    
    [result][nextjournal#output#68960eae-8344-4331-a419-cea794ee5480#result]
    
    # Big List of Stuff
    
    A ***stuff*** is a map of `:head`, `:term`, `:kind`, and `:form` for the approximately 227 heads & forms of ASR. A stuff is all we need for making clojure.specs from terms, heads, & forms. The stuff keywords `:head`, `:term`, `:kind`, and `:form` need not be namespaced.
    
    This  big list of stuff is like a big, flat, denormalized database table.
    
    ## Generalized Heads
    
    For composites, the "head" is obvious because it's a symbol followed by an args tuple.
    
    For symconsts, the "heads" are just the symbolic constants themselves.
    
    For all tuples, the head is gensymmed. Example: head `::asr-tuple3805` (kebab-case; exception to the rule for heads), corresponds to term `::alloc_arg`, in snake case, like all terms.
    
    ### Don't Kebab Too Early
    
    Heads, except for gensymmed heads for tuples, are in PascalCase; don't kebab them. We'll kebab the derived namespaced keywords for naming clojure.specs.
    
    ## Helper: Stuff from Term & Form
    
    Here we go again, illiterates! Gotta show you how we're doing it before showing you what we're doing!
    
    The intention is to partially evaluate `stuff-from-term-form` on a term, then map the result over all the forms for that term.
    
    ```clojure id=eaa857a3-9d94-414f-9394-54acd01bf557
    (defn kind-from-form [form]
      (-> form first first))
    (defn head-from-kind-form [kind form]
      (case kind
        :ASDL-COMPOSITE (-> form first second :ASDL-HEAD)
        :ASDL-SYMCONST (-> form first second) ;; symconst itself
        :ASDL-TUPLE (-> form first second)))
    (defn stuff-from-term-form [term form]
      (let [kind (-> form kind-from-form)
            ghead (head-from-kind-form kind form)
            kwh (keyword "asr" ghead)] ;; no kebab'bing
        {:head kwh,:term term,:kind kind,:form,form}))
    ```
    
    ```clojure id=6a754b5e-24be-4d05-88c5-e653c5ce4bad
    (def big-list-of-stuff
      (mapcat identity
        (map (fn [speclet]
             (let [[term forms] speclet
                   htkfs (map (partial stuff-from-term-form term) forms)]
               htkfs))
        big-map-of-speclets-from-terms)))
    ```
    
    [result][nextjournal#output#6a754b5e-24be-4d05-88c5-e653c5ce4bad#result]
    
    # All Symconst Specs
    
    Clojure.specs for symconsts are easiest because they don't depend on other clojure.specs. There are about 72 symconsts (more as ASR grows):
    
    ## Symconst Stuffs
    
    ```clojure id=abc8ee32-b0fe-469c-8c04-c70c3f2c569e
    (def symconst-stuffs
       (filter #(= (:kind %) :ASDL-SYMCONST) big-list-of-stuff))
    ```
    
    [result][nextjournal#output#abc8ee32-b0fe-469c-8c04-c70c3f2c569e#result]
    
    ## Symconst-Head-Specs
    
    This next code block INSTALLS the (about) 72 head-specs by `eval`'ing the `s/defs` written by `` `(s/def ...) ``. A spec is *installed* into a hidden Clojure Spec Registry by side-effect and is associated with the namespaced keyword produced by `nskw-kebab-from`. Once this next code block runs, we'll have (about) 72 head-specs magically installed and we can refer to them by namespaced kebab'bed keyword name. For example, `::implementation` will be installed and we can refer to it via `(s/spec ::implementation)`. 
    
    All specs, head-specs and term-specs alike must be installed before being referred-to. Later, we'll break co-recursive cycles by installing defective specs then backpatching them. For example, the term-spec for `::symbol` refers to the term-spec for `::symbol-table`, which refers to the term-spec for `::symbol`. Clojure.spec can't tolerate that, but it can tolerate a defective termsspec for `::symbol-table` that we backpatch later. 
    
    Construct and install all (approximately) 72 symconst head-specs:
    
    ```clojure id=82c3d607-5487-439b-9a69-2f18e938929b
    (defn spec-from-symconst-stuff [symconst-stuff]
      (let [symconst (-> symconst-stuff :form :ASDL-SYMCONST)
            nskw (nskw-kebab-from symconst)]
        `(s/def ~nskw #{(quote ~(symbol symconst))})))
    ;; side-effecting code: The value of this expression is
    ;; only for inspection.
    (->> symconst-stuffs
      (map spec-from-symconst-stuff)
      (map eval))  ;; SIDE-EFFECT! Install! Woo Hoo!
    ```
    
    [result][nextjournal#output#82c3d607-5487-439b-9a69-2f18e938929b#result]
    
    ### Unit Tests
    
    We see that each of the 72 head-specs is just a predicate for an unqualified symbol. The unqualified symbol `'Add` conforms to the head-spec `::add` in the `asr` namespace.
    
    ```clojure id=f1b41768-cc74-4d27-a958-78929defb755
    (s/conform (s/spec ::add) 'Add)
    ```
    
    Also, enjoy your first taste of a generator, trivial in this case, but instructive:
    
    ```clojure id=7dd2b67e-352d-400a-9de0-087202a0e907
    (gen/generate (s/gen ::add))
    ```
    
    ## Symconst-Term-Specs
    
    To check an instance or utterance of ASR like expr-221000, we'll need to check its sub-parts by term, not by head.
    
    ### Symconst Stuffss \[sic\] by Term
    
    First, partition the symconst specs by term. There are about 13 terms categorizing the (approx) 72 symconst heads.
    
    ```clojure id=dfae2600-bc53-44b4-a97f-c3758c2b85cd
    (def symconst-stuffss-by-term (partition-by :term symconst-stuffs))
    ```
    
    [result][nextjournal#output#dfae2600-bc53-44b4-a97f-c3758c2b85cd#result]
    
    ### Symconst Spec for Term \[sic\]
    
    For each term, write a `set` containing its alternative heads, e.g., the term `binop` is one of the ten heads `Add`, `Sub`, and so on, to `BitRShift`.
    
    To unit-test `spec-for-term`, `eval` one of them and check it:
    
    ```clojure id=73cb5487-9c13-42b4-a8ad-e5548ba2942b
    (defn symconst-spec-for-term [stuffs-for-term]
      (let [term (-> stuffs-for-term first :term) ;; same for all! TODO: assert
            term-nskw (nskw-kebab-from (name term))
            ss1
            (->> stuffs-for-term
              (map (fn [stuff]
                     (let [head (head-from-kind-form (:kind stuff) (:form stuff))]
                       (-> head symbol)))))]
        `(s/def ~term-nskw (set (quote ~ss1)))))  ;; Here is the 'set'!
    (def utest-symconst-term-spec
      (-> (nth symconst-stuffss-by-term 3)
        symconst-spec-for-term
        #_echo
        eval))
    (s/explain utest-symconst-term-spec 'Add)
    #_(s/exercise ::binop)  ;; every time you run you get different results
    ```
    
    ### Install
    
    To install the thirteen term-specs for symconsts, `eval` them.
    
    ```clojure id=60580897-7d67-4123-b709-e0dc94fc6961
    (->> symconst-stuffss-by-term
      (map symconst-spec-for-term)
      (map eval)) ;; SIDE-EFFECT! Woo Hoo!
    ```
    
    ### Unit Test
    
    ```clojure id=bfe11b21-7e69-4d77-9a47-6b70b7024d87
    (s/exercise ::trait)
    ```
    
    # Tuple Specs
    
    What do we want to see for a tuple head-spec? How about an `s/cat`?
    
    There are six tuple heads. Their names will change from run-to-run because the names are gensymmed.
    
    ```clojure id=5cf06789-ece6-4a36-9c6c-c22861604342
    (def tuple-stuffs
      (filter #(= (:kind %) :ASDL-TUPLE)
        big-list-of-stuff))
    ```
    
    [result][nextjournal#output#5cf06789-ece6-4a36-9c6c-c22861604342#result]
    
    We won't be able to test these until we have specs for *identifier*, *expr*, *symbol*, and *dimension.* Except for *identifier*, which isn't in ASR.asdl, we'll stub them now and backpatch them later.
    
    ## Spec for *identifier*
    
    We can't use just `symbol?` because it generates namespaced symbols, and they aren't useful for testing LPython. We'll need a custom generator (<https://clojure.org/guides/spec#_custom_generators>). 
    
    The following attempt has performance problems and will be discarded. We save it as a lesson in this kind of dead end.
    
    ```clojure id=a57ea154-1d58-4179-a401-bb061109363e
    (def identifier-re #"[a-zA-Z_][a-zA-Z0-9_]*")
    (s/def ::identifier
      (s/with-gen
        symbol?
        (fn [] (gen/such-that #(re-matches identifier-re (name %)) (gen/symbol)))))
    #_(s/exercise ::identifier 100) 
    ```
    
    We must, sadly, eliminate the solution above because it occasionally fails the *such-that*. Explore via exercising the candidate spec, say, 100 times (uncomment the expression above and evaluate the cell). 
    
    Here is a better solution that, sadly but harmlessly, lacks underscores.
    
    ```clojure id=0989a589-afd2-4f99-9ee6-cfe5671beeea
    (let [alpha-re #"[a-zA-Z]"  ;; The famous "let over lambda."
          alphameric-re #"[a-zA-Z0-9]*"]
      (def alpha?
        #(re-matches alpha-re %))
      (def alphameric?
        #(re-matches alphameric-re %))
      (defn identifier? [s]
        (and (alpha? (subs s 0 1))
          (alphameric? (subs s 1))))
      (def identifier-generator
        (tgen/let [c (gen/char-alpha)
                   s (gen/string-alphanumeric)]
          (str c s)))
      (s/def ::identifier  ;; side effects the spec registry!
        (s/with-gen
          identifier?
          (fn [] identifier-generator))))
    
    (s/exercise ::identifier #_100)
    ```
    
    ## Tuple-Term-Spec Stubs for *Expr*, *Symbol*, *Dimension*
    
    Exprs and symbols are composites, so we can expose a pattern for stub term-specs from these two. We'll choose a list with one of the valid head and zero or more randomly generated identifiers.
    
    ```clojure id=62d1bc11-9f80-4f51-a486-bafe26fa657c
    (defn heads-for-composite [term]
      (->> (term big-map-of-speclets-from-terms)
        (map :ASDL-COMPOSITE)
        (map :ASDL-HEAD)
        (map symbol)
        set))
    
    (defn generator-for-heads [heads]
      (tgen/let [head (s/gen heads)
                 rest (gen/list (s/gen ::identifier))]
        (cons head rest)))
    
    (defn lpred [heads]
      (s/and seq?
        (fn [lyst] (-> lyst count (>= 1)))
        (fn [lyst] (-> lyst first heads))))
    
    ;; The following doesn't work for unknown reason. 
    ;; Fails spec for 'let' when eval'ed. Some subtlety 
    ;; of the macrology of 'let.' Punt, but retain for
    ;; sake of instruction and TODO.
    #_(defn write-stub-spec-for-composite [term]
        `(let [heads (heads-for-composite ~term)]
         (s/def ~term
           (s/with-gen
             (lpred heads)
             (fn [] (generator-for-heads heads))))))
    
    #_(def symbol-stub-spec (write-stub-spec-for-composite ::symbol)) 
    #_(eval symbol-stub-spec)  ;; fails spec for 'let'
    
    ;; Would like to abstract the common pattern of the 
    ;; following two cases, but can't easily. See above.
    (let [heads (heads-for-composite ::symbol)]
      (s/def ::symbol
          (s/with-gen
            (lpred heads)
            (fn [] (generator-for-heads heads)))))
    
    (let [heads (heads-for-composite ::expr)]
      (s/def ::expr
          (s/with-gen
            (lpred heads)
            (fn [] (generator-for-heads heads)))))
    
    (s/exercise ::expr #_100) 
    ```
    
    A dimension is, itself, a tuple, so we'll have a weak stub spec at first.
    
    ```clojure id=5df0afae-c1df-41f8-bcbd-de4f36275c14
    (s/def ::dimension list?)
    ```
    
    ### Spec Fragment from Arg, Args
    
    Illiterates of the world, unite! Here is some "how-to" before the "what-for."
    
    Convert multiplicities into clojure.spec equivalents;
    
    ```clojure id=61909e52-e156-497c-b97b-cff0cda6c51f
    (defn spec-from-arg [arg]
      (let [type (nskw-kebab-from (:ASDL-TYPE arg))
            nym (:ASDL-NYM arg)]
        (case (:MULTIPLICITY arg)
          ::once `(s/spec ~type)
          ::at-most-once `(s/? (s/spec ~type))
          ::zero-or-more `(s/* (s/spec ~type)))))
    ```
    
    Just map over that:
    
    ```clojure id=91c30964-89f5-4cdf-89a1-b85f04cb17cb
    (defn spec-from-args [args]
      (let [nyms (->> args (map :ASDL-NYM) #_echo)
            kyms (->> nyms (map (comp keyword name)) #_echo)
            specules (->> args (map spec-from-arg) #_echo)
            riffle (-> (interleave kyms specules) #_echo)]
        `(s/cat ~@riffle)))
    ```
    
    ## Install Tuple-Head-Specs
    
    Notice the bang (`!`) on the end of the name of `spec-from-tuple-stuff!`. It doesn't really, itself, side-effect the Spec Registry, but its only use is to side-effect the Registry, so why not name it so?
    
    ```clojure id=7f5fca15-06d1-46d2-936b-50b766b11b83
    (defn spec-from-tuple-stuff! [tuple-stuff]
      (let [nskw (nskw-kebab-from (name (:head tuple-stuff)))
            args (-> tuple-stuff :form :ASDL-ARGS)]
        `(s/def ~nskw ~(spec-from-args args))))  ;; side effect!
    (->> tuple-stuffs
      (map spec-from-tuple-stuff!)
      echo
      (map eval))  ;; SIDE-EFFECT Woo Hoo! Bang Bang!
    ```
    
    ### Unit Tests
    
    You may have to modify these by hand because the gensyms may change every run:
    
    ```clojure id=76042bc7-a3f9-4605-82a5-1cec58263f6f
    (s/conform ::asr-tuple-3805 '((a b c) (f g h)))
    ```
    
    ```clojure id=586a8c8f-d821-496e-af7d-85451363eaa1
    (gen/generate (s/gen ::asr-tuple-3805))
    ```
    
    ## Tuple Term-Specs
    
    As before, we really need clojure.specs for the terms corresponding to the heads.
    
    ### Tuple Stuffss \[sic\] by Term
    
    ```clojure id=0ecf68b0-b6ca-4771-962d-969eaf239ce6
    (def tuple-stuffss-by-term (partition-by :term tuple-stuffs))
    ```
    
    [result][nextjournal#output#0ecf68b0-b6ca-4771-962d-969eaf239ce6#result]
    
    ### Tuple-Term-Spec
    
    ```clojure id=aae20034-2697-43c1-8f9f-c8a52c836b30
    (defn tuple-spec-for-term [stuffs]
      (let [term (-> stuffs first :term)
            term-nskw (nskw-kebab-from (name term))
            head (-> stuffs first :head name nskw-kebab-from)]
        `(s/def ~term-nskw (s/spec ~head))))
    ```
    
    ### Install
    
    To install the 6 term-specs, `eval` them.
    
    ```clojure id=af6218fc-c359-4faf-b8ee-da7b5e2a5f18
    (->> tuple-stuffss-by-term
      (map tuple-spec-for-term)
      (map eval))  ;; SIDE-EFFECT! Woo Hoo!
    ```
    
    ```clojure id=22532e4d-0b45-479a-b282-af17deef6a52
    (s/exercise ::dimension)
    ```
    
    [result][nextjournal#output#22532e4d-0b45-479a-b282-af17deef6a52#result]
    
    # Hand-Written Term Spec for SymbolTable
    
    ASDL doesn't offer an easy way to specify maps, but Clojure.spec does. ASR.asdl doesn't have a spec for `SymbolTable`, so we write one by hand and upgrade it as we go along. 
    
    We cannot define this spec until we define the others because `(s/spec ::symbol)` doesn't exist yet. We'll backpatch it later
    
    ```clojure id=79dae76d-9e2e-442c-a946-7948c4afae60
    (s/def ::symbol-table
      (s/cat
        :head #(= % 'SymbolTable)
        :unique-id int?
        :symbols (s/map-of keyword?
                   #_#(do % true) 
                   (s/spec ::symbol))))
    ```
    
    ```clojure id=fe81e0bc-24f9-40d3-a555-f4000eb4ab55
    (s/explain ::symbol-table '(SymbolTable 3 {}))
    ```
    
    But it's going to have to improve (also notice we may harmlessly surround the spec-name nskw in a call of `s/spec`):
    
    Let's check a real symbol table
    
    ```clojure id=83346640-b369-4d5b-8698-5ce6ea21cdd1
    (->> user/expr-01-211000 second echo (s/explain ::symbol-table))
    ```
    
    # Backpatching Symbol
    
    TODO
    
    # First Composite Spec: `TranslationUnit`
    
    We write specs as data lists and `eval` them later. Turns out it's necessary to do that, and it's a beneficial accident lest we clutter up the namespace of specs.
    
    As usual, because this is illiterate programming, we must define things before we can use them. Read the code backwards to get the big picture.
    
    Composites and tuples have lists of type-var pairs, that is, of args. We've already handled arg lists by defining `spec-from-args` above. 
    
    Specs for all tuples' heads and terms have already been installed.
    
    Specs for all symconsts' heads and terms have already been installed.
    
    ## Composite Head-Specs
    
    Composites have a head and a possibly empty list of args.
    
    ```clojure id=cabc5d67-ea28-4d57-8559-38c4a981c83e
    (defn spec-from-composite [composite]
      (let [head (-> composite :ASDL-HEAD symbol)
            nskw (-> head nskw-kebab-from #_echo)
            args (-> composite :ASDL-ARGS)]
        `(s/def ~nskw ~(spec-from-args args))))
    ```
    
    # TODO
    
    Automate the transformation of ASR instances from colon-following to colon-preceding form.
    
    [nextjournal#output#9be7df63-a594-451e-bc67-495cf6c8b55d#result]:
    <https://nextjournal.com/data/QmauZQqRJ6yJzhbbij6wzwPXsq4P5bPfk2m8ppddU1VhN1?content-type=application/transit%2Bjson&node-id=9be7df63-a594-451e-bc67-495cf6c8b55d&node-kind=output>
    
    [nextjournal#output#db3884f0-fd65-4f9d-9341-918c9e4733cd#result]:
    <https://nextjournal.com/data/QmTs3sSkGvToXgKLNFKLM9CNdoFe8fyyGJTTuuJWp1cy1A?content-type=application/transit%2Bjson&node-id=db3884f0-fd65-4f9d-9341-918c9e4733cd&node-kind=output>
    
    [nextjournal#output#cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f#result]:
    <https://nextjournal.com/data/QmX5ZSM5Snutx74is877viS1C4KSiMqWE3QvpcgGVtjtNU?content-type=application/transit%2Bjson&node-id=cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f&node-kind=output>
    
    [nextjournal#output#14995343-d18f-4579-b61f-96398c72c557#result]:
    <https://nextjournal.com/data/QmTa8u68FZ9WFKPTxq2JXYmJqawtdCUF2sNomp2ouZk5PC?content-type=application/transit%2Bjson&node-id=14995343-d18f-4579-b61f-96398c72c557&node-kind=output>
    
    [nextjournal#output#28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d#result]:
    <https://nextjournal.com/data/QmNhPv6rPt5dg2Lj9tEayy6gGTm2LsvABtCj321Wb6yHm5?content-type=application/transit%2Bjson&node-id=28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d&node-kind=output>
    
    [nextjournal#output#ef06350e-bcee-4e53-ac1f-d9975ed18fc6#result]:
    <https://nextjournal.com/data/QmTrvCgyJ2eAoxL7ApjGCMLKPePV5j7dyDGHiebPrigtcF?content-type=application/transit%2Bjson&node-id=ef06350e-bcee-4e53-ac1f-d9975ed18fc6&node-kind=output>
    
    [nextjournal#output#68960eae-8344-4331-a419-cea794ee5480#result]:
    <https://nextjournal.com/data/QmTTktsGAbhyw4PVFJQXKEEozMRj2hu51xLGfZbWLxVwsC?content-type=application/transit%2Bjson&node-id=68960eae-8344-4331-a419-cea794ee5480&node-kind=output>
    
    [nextjournal#output#6a754b5e-24be-4d05-88c5-e653c5ce4bad#result]:
    <https://nextjournal.com/data/QmYfBGcSAuBHvWK7b6U3wHv6RNPfjou2uQ5RfpjuB791Fr?content-type=application/transit%2Bjson&node-id=6a754b5e-24be-4d05-88c5-e653c5ce4bad&node-kind=output>
    
    [nextjournal#output#abc8ee32-b0fe-469c-8c04-c70c3f2c569e#result]:
    <https://nextjournal.com/data/QmNRAMYoSiNxpg7CRmfF6wNgh24uxiyBK6S6UWsPMLM6NE?content-type=application/transit%2Bjson&node-id=abc8ee32-b0fe-469c-8c04-c70c3f2c569e&node-kind=output>
    
    [nextjournal#output#82c3d607-5487-439b-9a69-2f18e938929b#result]:
    <https://nextjournal.com/data/QmPXpgYXAUsRNRFbuabAF7y3MrtvPVQk5RJWwnJj3LeSi5?content-type=application/transit%2Bjson&node-id=82c3d607-5487-439b-9a69-2f18e938929b&node-kind=output>
    
    [nextjournal#output#dfae2600-bc53-44b4-a97f-c3758c2b85cd#result]:
    <https://nextjournal.com/data/Qma13YzbSMCLgddf4FJCacHMrudTrwr64CNb3q7jxXkrGM?content-type=application/transit%2Bjson&node-id=dfae2600-bc53-44b4-a97f-c3758c2b85cd&node-kind=output>
    
    [nextjournal#output#5cf06789-ece6-4a36-9c6c-c22861604342#result]:
    <https://nextjournal.com/data/QmTpKxfnoDzZpioE3uSn7L1SnBMkfTb7UD9ofuAnTaFyWm?content-type=application/transit%2Bjson&node-id=5cf06789-ece6-4a36-9c6c-c22861604342&node-kind=output>
    
    [nextjournal#output#0ecf68b0-b6ca-4771-962d-969eaf239ce6#result]:
    <https://nextjournal.com/data/QmWHDTSjPJAWuU4xNhs4QsWuuZBX8W7tFqfAwSFjxiSniT?content-type=application/transit%2Bjson&node-id=0ecf68b0-b6ca-4771-962d-969eaf239ce6&node-kind=output>
    
    [nextjournal#output#22532e4d-0b45-479a-b282-af17deef6a52#result]:
    <https://nextjournal.com/data/QmenvyfpYcvY9ThxAtqBsYMKVKAY3Qd32kUZvkvVf9JxwZ?content-type=application/transit%2Bjson&node-id=22532e4d-0b45-479a-b282-af17deef6a52&node-kind=output>
    
    <details id="com.nextjournal.article">
    <summary>This notebook was exported from <a href="https://nextjournal.com/a/FnEMAE1Pkx2vWFMH6NVpJX?change-id=DF98dM4TZN9i8X5ATYF4Ge">https://nextjournal.com/a/FnEMAE1Pkx2vWFMH6NVpJX?change-id=DF98dM4TZN9i8X5ATYF4Ge</a></summary>
    
    ```edn nextjournal-metadata
    {:article
     {:settings {:numbered? true},
      :nodes
      {"029fe8f0-78f1-4cf8-8271-807e090e83a4"
       {:compute-ref #uuid "bd1eac68-4e49-4cb2-a412-cbdfc0537a7d",
        :exec-duration 516,
        :id "029fe8f0-78f1-4cf8-8271-807e090e83a4",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "0989a589-afd2-4f99-9ee6-cfe5671beeea"
       {:compute-ref #uuid "bbe4315b-df8e-405d-b013-78b813f890be",
        :exec-duration 42,
        :id "0989a589-afd2-4f99-9ee6-cfe5671beeea",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "0a784b7a-e707-41fa-8598-d4a4586c77c6"
       {:compute-ref #uuid "b4af3987-9893-40e3-b892-35818edae6a7",
        :exec-duration 381,
        :id "0a784b7a-e707-41fa-8598-d4a4586c77c6",
        :kind "code",
        :output-log-lines {:stdout 15},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "0ecf68b0-b6ca-4771-962d-969eaf239ce6"
       {:compute-ref #uuid "74dc4d7a-af2c-4113-93ac-2a43ef9f819b",
        :exec-duration 330,
        :id "0ecf68b0-b6ca-4771-962d-969eaf239ce6",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "14995343-d18f-4579-b61f-96398c72c557"
       {:compute-ref #uuid "6f72842d-3d94-42e2-a372-59fa48b284d0",
        :exec-duration 156,
        :id "14995343-d18f-4579-b61f-96398c72c557",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "17507f3b-6ac2-47d1-91e3-260161097282"
       {:compute-ref #uuid "9ae96c51-22ac-4229-9a77-686cffc6d80b",
        :exec-duration 626,
        :id "17507f3b-6ac2-47d1-91e3-260161097282",
        :kind "code",
        :output-log-lines {:stdout 110},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "22532e4d-0b45-479a-b282-af17deef6a52"
       {:compute-ref #uuid "904ea41f-4972-4f2b-b3c9-464e632cc924",
        :exec-duration 413,
        :id "22532e4d-0b45-479a-b282-af17deef6a52",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d"
       {:compute-ref #uuid "7046b19e-567a-4dcb-8a89-64dcbaebb3a2",
        :exec-duration 1997,
        :id "28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "29552ba9-d499-4842-9448-63608ce24e24"
       {:environment
        [:environment
         {:article/nextjournal.id
          #uuid "5b45eb52-bad4-413d-9d7f-b2b573a25322",
          :change/nextjournal.id
          #uuid "6140750b-27b0-4b4d-86f3-b07682cd65c6",
          :node/id "0ae15688-6f6a-40e2-a4fa-52d81371f733"}],
        :id "29552ba9-d499-4842-9448-63608ce24e24",
        :kind "runtime",
        :language "clojure",
        :type :prepl,
        :runtime/mounts
        [{:src [:node "ffcf0396-b3f9-40e6-a0c2-654401879781"],
          :dest "/deps.edn"}]},
       "4fb2c34f-9857-4ec8-bdea-f6776d3093c1"
       {:compute-ref #uuid "618e6e8c-ffc2-4c92-95d2-f22e6a6affa7",
        :exec-duration 19,
        :id "4fb2c34f-9857-4ec8-bdea-f6776d3093c1",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "586a8c8f-d821-496e-af7d-85451363eaa1"
       {:compute-ref #uuid "d502154c-52b3-4598-8549-3b56d3be4581",
        :exec-duration 26,
        :id "586a8c8f-d821-496e-af7d-85451363eaa1",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "5cf06789-ece6-4a36-9c6c-c22861604342"
       {:compute-ref #uuid "fb1822f5-1465-4e5d-9cae-5cffd27d5ba8",
        :exec-duration 323,
        :id "5cf06789-ece6-4a36-9c6c-c22861604342",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "5df0afae-c1df-41f8-bcbd-de4f36275c14"
       {:compute-ref #uuid "e4f8cd3a-4191-4fe3-a174-2735582d14a8",
        :exec-duration 8,
        :id "5df0afae-c1df-41f8-bcbd-de4f36275c14",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "60580897-7d67-4123-b709-e0dc94fc6961"
       {:compute-ref #uuid "62b3cca2-51d7-4039-98c9-a09e29494463",
        :exec-duration 13,
        :id "60580897-7d67-4123-b709-e0dc94fc6961",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "60ca7c24-976f-45e5-921f-311004fb1ff4"
       {:compute-ref #uuid "94389b98-1511-43ec-855a-b204eba59342",
        :exec-duration 90,
        :id "60ca7c24-976f-45e5-921f-311004fb1ff4",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "61909e52-e156-497c-b97b-cff0cda6c51f"
       {:compute-ref #uuid "d2afd08a-4b83-4656-945a-4ccb7c1b9a9f",
        :exec-duration 19,
        :id "61909e52-e156-497c-b97b-cff0cda6c51f",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "62d1bc11-9f80-4f51-a486-bafe26fa657c"
       {:compute-ref #uuid "9082caf8-0e30-4e73-ab01-a400d32f38c8",
        :exec-duration 67,
        :id "62d1bc11-9f80-4f51-a486-bafe26fa657c",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "68960eae-8344-4331-a419-cea794ee5480"
       {:compute-ref #uuid "cebe997d-593b-447d-9c59-3c2b53f2be33",
        :exec-duration 451,
        :id "68960eae-8344-4331-a419-cea794ee5480",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "6a635fa0-719a-4eb6-9698-1ed0488244f7"
       {:compute-ref #uuid "c5155cfc-cc05-40ae-a37f-be14eaba1c13",
        :exec-duration 370,
        :id "6a635fa0-719a-4eb6-9698-1ed0488244f7",
        :kind "code",
        :output-log-lines {:stdout 6},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "6a754b5e-24be-4d05-88c5-e653c5ce4bad"
       {:compute-ref #uuid "f7e4b97a-96c4-4940-ab77-1b39c3f0d7fb",
        :exec-duration 414,
        :id "6a754b5e-24be-4d05-88c5-e653c5ce4bad",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "711cc44d-616c-4d69-a01e-5138898ee4e2"
       {:compute-ref #uuid "181576d3-a1eb-453c-8193-e1f05110ab6a",
        :exec-duration 332,
        :id "711cc44d-616c-4d69-a01e-5138898ee4e2",
        :kind "code",
        :output-log-lines {:stdout 21},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "73cb5487-9c13-42b4-a8ad-e5548ba2942b"
       {:compute-ref #uuid "e8794ed2-584e-4b8b-8d3b-d2c0b7a2df31",
        :exec-duration 297,
        :id "73cb5487-9c13-42b4-a8ad-e5548ba2942b",
        :kind "code",
        :output-log-lines {:stdout 2},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "76042bc7-a3f9-4605-82a5-1cec58263f6f"
       {:compute-ref #uuid "88438521-811e-4596-831a-9d99755d4fe6",
        :exec-duration 10,
        :id "76042bc7-a3f9-4605-82a5-1cec58263f6f",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "79dae76d-9e2e-442c-a946-7948c4afae60"
       {:compute-ref #uuid "db14a51e-5e69-4ef3-b334-6fbed8f1b712",
        :exec-duration 11,
        :id "79dae76d-9e2e-442c-a946-7948c4afae60",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "7dd2b67e-352d-400a-9de0-087202a0e907"
       {:compute-ref #uuid "cbd8eb5b-f75e-4566-8a3b-e3b114745516",
        :exec-duration 4,
        :id "7dd2b67e-352d-400a-9de0-087202a0e907",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "7f5fca15-06d1-46d2-936b-50b766b11b83"
       {:compute-ref #uuid "f65936cd-db6c-40e5-aea0-7f1e771af958",
        :exec-duration 441,
        :id "7f5fca15-06d1-46d2-936b-50b766b11b83",
        :kind "code",
        :output-log-lines {:stdout 45},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "82c3d607-5487-439b-9a69-2f18e938929b"
       {:compute-ref #uuid "f80fe423-16fe-41dd-979a-f04253bfa450",
        :exec-duration 117,
        :id "82c3d607-5487-439b-9a69-2f18e938929b",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "83346640-b369-4d5b-8698-5ce6ea21cdd1"
       {:compute-ref #uuid "feb4e0e8-8b8c-4dad-8d23-604b15cb8775",
        :exec-duration 425,
        :id "83346640-b369-4d5b-8698-5ce6ea21cdd1",
        :kind "code",
        :output-log-lines {:stdout 109},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "91c30964-89f5-4cdf-89a1-b85f04cb17cb"
       {:compute-ref #uuid "57a265f8-9e26-44ed-8a82-f53a6e50de46",
        :exec-duration 9,
        :id "91c30964-89f5-4cdf-89a1-b85f04cb17cb",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "9be7df63-a594-451e-bc67-495cf6c8b55d"
       {:compute-ref #uuid "5afa1031-4234-4fb8-b328-95e020b73d51",
        :exec-duration 70,
        :id "9be7df63-a594-451e-bc67-495cf6c8b55d",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "a57ea154-1d58-4179-a401-bb061109363e"
       {:compute-ref #uuid "94465df7-c93d-48ad-b3b7-98279e751b8c",
        :exec-duration 8,
        :id "a57ea154-1d58-4179-a401-bb061109363e",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "aae20034-2697-43c1-8f9f-c8a52c836b30"
       {:compute-ref #uuid "44d26af9-f7e9-4ae6-8a53-b79ecbf65c9e",
        :exec-duration 50,
        :id "aae20034-2697-43c1-8f9f-c8a52c836b30",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "abc8ee32-b0fe-469c-8c04-c70c3f2c569e"
       {:compute-ref #uuid "608be9a7-0838-4849-9e0b-52082175833f",
        :exec-duration 57,
        :id "abc8ee32-b0fe-469c-8c04-c70c3f2c569e",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "af6218fc-c359-4faf-b8ee-da7b5e2a5f18"
       {:compute-ref #uuid "76fc5b31-9c03-4782-9877-e4d4480d45df",
        :exec-duration 25,
        :id "af6218fc-c359-4faf-b8ee-da7b5e2a5f18",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "af906587-480d-4f71-855c-e803e5cba1d5"
       {:compute-ref #uuid "e0da7f46-bd3e-4cfb-8abd-76aa158a8ab1",
        :exec-duration 28,
        :id "af906587-480d-4f71-855c-e803e5cba1d5",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "bfe11b21-7e69-4d77-9a47-6b70b7024d87"
       {:compute-ref #uuid "2e663f6f-49b8-4658-bc25-f6e206342829",
        :exec-duration 17,
        :id "bfe11b21-7e69-4d77-9a47-6b70b7024d87",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "cabc5d67-ea28-4d57-8559-38c4a981c83e"
       {:compute-ref #uuid "4aab1520-16ba-498e-b841-a9b91ff04132",
        :exec-duration 20,
        :id "cabc5d67-ea28-4d57-8559-38c4a981c83e",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f"
       {:compute-ref #uuid "53f2acbb-1917-417a-bc8e-cfd8cf852b1e",
        :exec-duration 74,
        :id "cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "d9f6c457-f4d7-4565-b8d2-0039b3aaf888"
       {:environment
        [:environment
         {:node/id "0149f12a-08de-4f3d-9fd3-4b7a665e8624",
          :article/nextjournal.id
          #uuid "5b45e08b-5b96-413e-84ed-f03b5b65bd66",
          :change/nextjournal.id
          #uuid "6034be04-2bc2-4468-af0e-cd7b9b6e7ed8"}],
        :id "d9f6c457-f4d7-4565-b8d2-0039b3aaf888",
        :kind "runtime",
        :language "python",
        :type :jupyter},
       "db3884f0-fd65-4f9d-9341-918c9e4733cd"
       {:compute-ref #uuid "c5da9add-2648-4c5c-8294-37c617294cd1",
        :exec-duration 425,
        :id "db3884f0-fd65-4f9d-9341-918c9e4733cd",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "db8dcc66-f14b-4344-9205-9c3f9ab20ee6"
       {:compute-ref #uuid "179f65ad-3943-49ea-ab82-2e0fe06e03f3",
        :exec-duration 36,
        :id "db8dcc66-f14b-4344-9205-9c3f9ab20ee6",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "dfae2600-bc53-44b4-a97f-c3758c2b85cd"
       {:compute-ref #uuid "100ec601-af2e-4ace-a9a9-9c4d9ccbc3db",
        :exec-duration 57,
        :id "dfae2600-bc53-44b4-a97f-c3758c2b85cd",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "eaa857a3-9d94-414f-9394-54acd01bf557"
       {:compute-ref #uuid "e6ee6bd3-92e7-4dcf-9423-4fee55f3dd01",
        :exec-duration 19,
        :id "eaa857a3-9d94-414f-9394-54acd01bf557",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "ef06350e-bcee-4e53-ac1f-d9975ed18fc6"
       {:compute-ref #uuid "11b3085f-23b6-40f2-a12e-23cc489b201b",
        :exec-duration 536,
        :id "ef06350e-bcee-4e53-ac1f-d9975ed18fc6",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "f1020f8e-d252-4b90-b78a-e74a366b580e"
       {:compute-ref #uuid "24df8f2f-57ee-456c-b9f3-4ea080fe6eb1",
        :exec-duration 454,
        :id "f1020f8e-d252-4b90-b78a-e74a366b580e",
        :kind "code",
        :output-log-lines {:stdout 2},
        :runtime [:runtime "d9f6c457-f4d7-4565-b8d2-0039b3aaf888"]},
       "f1b41768-cc74-4d27-a958-78929defb755"
       {:compute-ref #uuid "2c59f782-9120-4bda-b145-0165200e3fa8",
        :exec-duration 6,
        :id "f1b41768-cc74-4d27-a958-78929defb755",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "fe81e0bc-24f9-40d3-a555-f4000eb4ab55"
       {:compute-ref #uuid "4b4c2b41-e070-48d5-b525-54c8a77b97df",
        :exec-duration 324,
        :id "fe81e0bc-24f9-40d3-a555-f4000eb4ab55",
        :kind "code",
        :output-log-lines {:stdout 2},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "ffcf0396-b3f9-40e6-a0c2-654401879781"
       {:id "ffcf0396-b3f9-40e6-a0c2-654401879781",
        :kind "code-listing",
        :name "deps.edn"}},
      :nextjournal/id #uuid "77b0a2f9-a708-4e51-8d1d-4393b7bd4a64",
      :article/change
      {:nextjournal/id #uuid "63271681-5796-4a29-a938-65429c974a97"}}}
    
    ```
    </details>
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/.ipynb_checkpoints/genetically-engineered-asr.nextjournal-checkpoint.md">
<!-- #endraw -->

```markdown
<block name="genetically-engineered-asr.nextjournal-checkpoint_05BF0E"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

## genetically-engineered-asr.nextjournal.md

<!-- #raw -->
<noweb name="genetically-engineered-asr.nextjournal_2FF0A2">
<!-- #endraw -->

    # Genetically Engineered ASR
    
    Let's generate bits of ASR for testing purposes. Eventually, we'll evolve a big population of generated ASR, with "fitness" measuring "tendency to find bugs."
    
    We'll need a `clojure.spec` for `test.check` to generate ASR instances. Let's generate the `clojure.spec` from the ASDL spec [https://github.com/lcompilers/lpython/blob/84a073ce44a9a74213a4ac5648ee783bd38fc90f/src/libasr/ASR.asdl](https://github.com/lcompilers/lpython/blob/84a073ce44a9a74213a4ac5648ee783bd38fc90f/src/libasr/ASR.asdl#L87-L90) 
    
    # Mechanics
    
    Transition to Tangledown and Tangleup, 18 Sept 2022. This notebook now takes over 1 minute to boot up. I am going to experiment with a literate notebook. Caveats: clojure kernel does NOT work in jupyter lab, so TangleUp will be necessary to maintain the notebook. First step: export this as markdown. Here goes! See you back here later after my experiments!
    
    # Prelude
    
    ## Dependencies
    
    We include *core.logic* for experimentation. `Instaparse` is for parsing. Swiss arrows are just fun. `Camel-snake-kebab` is for naming conventions. `compliment` is for autocompletion in the notebook. 
    
    ```edn no-exec id=ffcf0396-b3f9-40e6-a0c2-654401879781
    {:deps {org.clojure/clojure {:mvn/version "1.11.1"}
            org.clojure/core.logic {:mvn/version "1.0.1"}
            org.clojure/test.check {:mvn/version "1.1.1"}
            instaparse {:mvn/version "1.4.12"}
            swiss-arrows {:mvn/version "0.6.0"}
            camel-snake-kebab {:mvn/version "0.4.3"}
            ;; compliment is for autocompletion in the notebook
            ;; add your libs here (and restart the runtime to pick up changes)
            compliment/compliment {:mvn/version "0.3.9"} } }
    ```
    
    ## Imports
    
    We'll get started in the `user` namespace, just poking around.
    
    ```clojure id=af906587-480d-4f71-855c-e803e5cba1d5
    (require '[clojure.spec.alpha :as s])
    (require '[clojure.pprint])
    (def pp clojure.pprint/pprint)
    (require '[instaparse.core :as insta])
    (require '[clojure.zip :as zip])
    ```
    
    # Motivating Example ASR
    
    Here is an example datum, a tree of ASR from  <https://raw.githubusercontent.com/lcompilers/lpython/main/tests/reference/asr-expr_01-211000e.stdout>. The syntax of this datum is *almost* Clojure: we must move colons from the backs of keys to the fronts. Clojure won't even *read* a symbol followed by a colon, but Clojure interprets a colon followed by a symbol as a Clojure keyword. Those are really convenient. Amongst other things, they're lookup functions in hashmaps.
    
    I'll move the colons by hand, aided by <https://regex101.com/r/kUW4Ug/1>. TODO: with instaparse.
    
    ## ASR for expr_01.py:
    
    Cut and paste, after moving the colons from back to front. It's too long to look at in the notebook, but ...
    
    ```clojure id=9be7df63-a594-451e-bc67-495cf6c8b55d
    (def expr-01-211000 '(TranslationUnit (SymbolTable 1 {:_lpython_main_program (Function (SymbolTable 4 {}) _lpython_main_program [] [] [(SubroutineCall 1 main0 () [] ())] () Source Public Implementation () .false. .false. .false. .false.),:main0 (Function (SymbolTable 2 {:x (Variable 2 x Local () () Default (Integer 4 []) Source Public Required .false.),:x2 (Variable 2 x2 Local () () Default (Integer 8 []) Source Public Required .false.),:y (Variable 2 y Local () () Default (Real 4 []) Source Public Required .false.),:y2 (Variable 2 y2 Local () () Default (Real 8 []) Source Public Required .false.)}) main0 [] [] [(= (Var 2 x) (IntegerBinOp (IntegerBinOp (IntegerConstant 2 (Integer 4 [])) Add (IntegerConstant 3 (Integer 4 [])) (Integer 4 []) (IntegerConstant 5 (Integer 4 []))) Mul (IntegerConstant 5 (Integer 4 [])) (Integer 4 []) (IntegerConstant 25 (Integer 4 []))) ()) (Print () [(Var 2 x)] () ())] () Source Public Implementation () .false. .false. .false. .false.),:main_program (Program (SymbolTable 3 {}) main_program [] [(SubroutineCall 1 _lpython_main_program () [] ())])}) []))
    ```
    
    [result][nextjournal#output#9be7df63-a594-451e-bc67-495cf6c8b55d#result]
    
    Click the tiny right triangle above to see what's in the list. Or, pretty-print it:
    
    ```clojure id=17507f3b-6ac2-47d1-91e3-260161097282
    (pp expr-01-211000)
    ```
    
    By the way, here is the Python that generates the ASR above, from <https://github.com/lcompilers/lpython/blob/84a073ce44a9a74213a4ac5648ee783bd38fc90f/tests/expr_01.py>.
    
    ```python id=f1020f8e-d252-4b90-b78a-e74a366b580e
    def main0():
        x: i32
        x2: i64
        y: f32
        y2: f64
        x = (2+3)*5
        print(x)
    
    main0()
    ```
    
    ## Does the Example Conform to Spec?
    
    *expr-01-211000* is a Clojure Persistent List:
    
    ```clojure id=db3884f0-fd65-4f9d-9341-918c9e4733cd
    (type expr-01-211000)
    ```
    
    [result][nextjournal#output#db3884f0-fd65-4f9d-9341-918c9e4733cd#result]
    
    Write a spec that tests that fact and smoke-test the clojure.spec library:
    
    ```clojure id=cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f
    (s/conform list? expr-01-211000)
    ```
    
    [result][nextjournal#output#cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f#result]
    
    ## Namespace Imports
    
    Once we enter the `asr` namespace via `(ns asr)`, we must again import things we're going to use. We must qualify the expression `expr-01-211000` by the *user* namespace like this: `user/expr-01-211000`; `expr-01-211000` is not in `asr`, it's in `user`.
    
    We can only name clojure.specs with namespaced keywords like `::foo` or `:asr/bar` (<https://blog.jeaye.com/2017/10/31/clojure-keywords/>). 
    
    ```clojure id=60ca7c24-976f-45e5-921f-311004fb1ff4
    (ns asr) ;; enter the namespace implicitly
    (require '[clojure.spec.alpha :as s])
    (require '[clojure.pprint])
    (def pp clojure.pprint/pprint)
    (defn echo [x] (pp x) x)  ;; TODO: macro?
    (require '[instaparse.core :as insta])
    (require '[clojure.zip :as zip])
    (require '[camel-snake-kebab.core :as csk])
    (require '[clojure.spec.gen.alpha :as gen])
    (require '[clojure.spec.test.alpha :as stest])
    (require '[clojure.test.check.generators :as tgen])
    ```
    
    ### Kebab'bed Namespaced Keywords for Specs from Symbols in ASR
    
    Transform conventional names in ASR PascalCase to conventional namespaced keywords in kebab-case in clojure.spec. It works on symbols or on strings. We can write a spec for this function, too? Specs all the way down!
    
    ```clojure id=db8dcc66-f14b-4344-9205-9c3f9ab20ee6
    (defn nskw-kebab-from  ;; TODO: macro?
      [sym-or-string]  
      (keyword "asr" (name (csk/->kebab-case sym-or-string)))
      ;; Found by experiment that ->> doesn't work, here.
      #_(->> sym csk/->kebab-case #(keyword "asr" %)) )
    (s/fdef nskw-kebab-from
      :args (s/alt :str string? :sym symbol?)
      :ret keyword?)
    (stest/instrument `nskw-kebab-from)
    
    (nskw-kebab-from 'TranslationUnit)
    (nskw-kebab-from "TranslationUnit")
    ;(nskw-kebab-from 42)
    ```
    
    # A Grammar for ASDL Specs
    
    ## ASDL Spec for ASR
    
    Here is a big string that contains the ASR.asdl, the spec that any ASR instance must conform to. I had to escape the double-quote marks by hand.
    
    ```clojure id=14995343-d18f-4579-b61f-96398c72c557
    (def all-asr "-- Abstract Semantic Representation (ASR) definition
    
    -- The aim of ASR is to represent all semantics in a non-redundant way, and that
    -- has all the semantic information available locally, so that the backend can
    -- do a single pass over ASR and have all the information at hand to generate
    -- code.
    --
    -- ASR is always semantically valid Fortran code. It is as far from the original
    -- Fortran language code as possible (i.e. everything is explicitly figured out,
    -- all semantic information gathered and readily available locally from each ASR
    -- node), while ensuring no semantic information was lost (no lowering was
    -- done), so one can still generate Fortran code from ASR that will be logically
    -- equivalent to the original code.
    --
    -- ASR can be used to do Fortran level transformations (such as optimizations).
    
    -- ASDL's builtin types are:
    --   * identifier
    --   * int (signed integers of infinite precision)
    --   * string
    -- We extend these by:
    --   * bool (.true. / .false.)
    --   * float (floating point number of infinite precision)
    --   * symbol_table (scoped Symbol Table implementation)
    --   * node (any ASR node)
    --
    -- Note: `symbol_table` contains `identifier` -> `symbol` mappings.
    
    module ASR {
    
    unit
        = TranslationUnit(symbol_table global_scope, node* items)
    
    -- # Documentation for the symbol type
    
    -- Each symbol has either `symtab` (local symbol table) or `parent_symtab`
    -- (where this symbol is stored). One can get to parent_symtab via symtab, so
    -- only one is present.
    
    -- Each symbol has a `name` for easy lookup of the name of the symbol when only
    -- having a pointer to it.
    
    -- abi=Source means the symbol's implementation is included (full ASR),
    -- otherwise it is external (interface ASR, such as procedure interface).
    
    -- SubroutineCall/FunctionCall store the actual final resolved subroutine or
    -- function (`name` member). They also store the original symbol
    -- (`original_name`), which can be one of: null, GenericProcedure or
    -- ExternalSymbol.
    
    -- When a module is compiled, it is parsed into full ASR, an object file is
    -- produced, the full ASR (abi=Source, \" body\" is non-empty) is transformed into
    -- interface ASR (abi=LFortran, \"body\" is empty). Both interface and full ASR
    -- is saved into the mod file.
    
    -- When a module is used, it is first looked up in the symbol table (as either
    -- full or interface ASR) and used if it is present. Otherwise a mod file is
    -- found on the disk, loaded (as either full or interface ASR for LFortran's
    -- mod file, depending on LFortran's compiler options; or for GFortran's mod
    -- file the corresponding interface ASR is constructed with abi=GFortran) and
    -- used. After the ASR is loaded, the symbols that are used are represented as
    -- ExternalSymbols in the current scope of the symbol table.
    
    -- ExternalSymbol represents symbols that cannot be looked up in the current
    -- scoped symbol table. As an example, if a variable is defined in a module,
    -- but used in a nested subroutine, that is not an external symbol
    -- because it can be resolved in the current symbol table (nested subroutine)
    -- by following the parents. However if a symbol is used from a different
    -- module, then it is an external symbol, because usual symbol resolution by
    -- going to the parents will not find the definition. The `module_name` member
    -- is the name of the module the symbol is in, the `scope_names` is a list of
    -- names if the symbol is in a nested symbol table. For example if it is a
    -- local variable in a function `f` that is nested in function `g`, then
    -- `scope_names=[g, f]`.
    
    -- REPL: each cell is parsed into full ASR, compiled + executed, the full ASR
    -- is transformed into interface ASR (abi=LFortran) and kept in the symbol
    -- table. A new cell starts with an empty symbol table, whose parent symbol
    -- table is the previous cell. That allows function / declaration shadowing.
    
    
    symbol
        = Program(symbol_table symtab, identifier name, identifier* dependencies,
            stmt* body)
        | Module(symbol_table symtab, identifier name, identifier* dependencies,
            bool loaded_from_mod, bool intrinsic)
        | Function(symbol_table symtab, identifier name, expr* args,
            ttype* type_params, stmt* body, expr? return_var, abi abi,
            access access, deftype deftype, string? bindc_name, bool elemental,
            bool pure, bool module, bool inline)
        | GenericProcedure(symbol_table parent_symtab, identifier name,
            symbol* procs, access access)
        | CustomOperator(symbol_table parent_symtab, identifier name,
            symbol* procs, access access)
        | ExternalSymbol(symbol_table parent_symtab, identifier name,
            symbol external, identifier module_name, identifier* scope_names,
            identifier original_name, access access)
        | DerivedType(symbol_table symtab, identifier name, identifier* members,
            abi abi, access access, symbol? parent)
        | EnumType(symbol_table symtab, identifier name, identifier* members,
            abi abi, access access, ttype type, symbol? parent)
        | Variable(symbol_table parent_symtab, identifier name, intent intent,
            expr? symbolic_value, expr? value, storage_type storage, ttype type,
            abi abi, access access, presence presence, bool value_attr)
        | ClassType(symbol_table symtab, identifier name, abi abi, access access)
        | ClassProcedure(symbol_table parent_symtab, identifier name, identifier
            proc_name, symbol proc, abi abi)
        | AssociateBlock(symbol_table symtab, identifier name, stmt* body)
        | Block(symbol_table symtab, identifier name, stmt* body)
    
    storage_type = Default | Save | Parameter | Allocatable
    access = Public | Private
    intent = Local | In | Out | InOut | ReturnVar | Unspecified
    deftype = Implementation | Interface
    presence = Required | Optional
    
    -- # Documentation for the ABI type
    
    -- External Yes: the symbol's implementation is not part of ASR, the
    -- symbol is just an interface (e.g., subroutine/function interface, or variable
    -- marked as external, not allocated by this ASR).
    
    -- External No:  the symbol's implementation is part of ASR (e.g.,
    -- subroutine/function body is included, variables must be allocated).
    
    -- abi=Source: The symbol's implementation is included in ASR, the backend is
    -- free to use any ABI it wants (it might also decide to inline or eliminate
    -- the code in optimizations).
    
    -- abi=LFortranModule/GFortranModule/BindC: the symbol's implementation is
    -- stored as machine code in some object file that needs to be linked in. It
    -- uses the specified ABI (one of LFortran module, GFortran module or C ABI).
    -- An interface that uses `iso_c_binding` and `bind(c)` is represented using
    -- abi=BindC.
    
    -- abi=Interactive: the symbol's implementation has been provided by the
    -- previous REPL execution (e.g., if LLVM backend is used for the interactive
    -- mode, the previous execution generated machine code for this symbol's
    -- implementation that was loaded into memory). Note: this option might be
    -- converted/eliminated to just use LFortran ABI in the future.
    
    -- abi=Intrinsic: the symbol's implementation is implicitly provided by the
    -- language itself as an intrinsic function. That means the backend is free to
    -- implement it in any way it wants. The function does not have a body, it is
    -- just an interface.
    
    abi                   -- External     ABI
        = Source          --   No         Unspecified
        | LFortranModule  --   Yes        LFortran
        | GFortranModule  --   Yes        GFortran
        | BindC           --   Yes        C
        | Interactive     --   Yes        Unspecified
        | Intrinsic       --   Yes        Unspecified
    
    
    stmt
        = Allocate(alloc_arg* args, expr? stat, expr? errmsg, expr? source)
        | Assign(int label, identifier variable)
        | Assignment(expr target, expr value, stmt? overloaded)
        | Associate(expr target, expr value)
        | Cycle()
        -- deallocates if allocated otherwise throws a runtime error
        | ExplicitDeallocate(symbol* vars)
        -- deallocates if allocated otherwise does nothing
        | ImplicitDeallocate(symbol* vars)
        | DoConcurrentLoop(do_loop_head head, stmt* body)
        | DoLoop(do_loop_head head, stmt* body)
        | ErrorStop(expr? code)
        | Exit()
        | ForAllSingle(do_loop_head head, stmt assign_stmt)
            -- GoTo points to a GoToTarget with the corresponding target_id within
            -- the same procedure. We currently use `int` IDs to link GoTo with
            -- GoToTarget to avoid issues with serialization.
        | GoTo(int target_id)
            -- An empty statement, a target of zero or more GoTo statements
            -- the `id` is only unique within a procedure
        | GoToTarget(int id)
        | If(expr test, stmt* body, stmt* orelse)
        | IfArithmetic(expr test, int lt_label, int eq_label, int gt_label)
        | Print(expr? fmt, expr* values, expr? separator, expr? end)
        | FileOpen(int label, expr? newunit, expr? filename, expr? status)
        | FileClose(int label, expr? unit, expr? iostat, expr? iomsg, expr? err, expr? status)
        | FileRead(int label, expr? unit, expr? fmt, expr? iomsg, expr? iostat, expr? id, expr* values)
        | FileRewind(int label, expr? unit, expr? iostat, expr? err)
        | FileInquire(int label, expr? unit, expr? file, expr? iostat, expr? err,
                  expr? exist, expr? opened, expr? number, expr? named,
                  expr? name, expr? access, expr? sequential, expr? direct,
                  expr? form, expr? formatted, expr? unformatted, expr? recl,
                  expr? nextrec, expr? blank, expr? position, expr? action,
                  expr? read, expr? write, expr? readwrite, expr? delim,
                  expr? pad, expr? flen, expr? blocksize, expr? convert,
                  expr? carriagecontrol, expr? iolength)
        | FileWrite(int label, expr? unit, expr? fmt, expr? iomsg, expr? iostat, expr? id, expr* values, expr? separator, expr? end)
        | Return()
        | Select(expr test, case_stmt* body, stmt* default)
        | Stop(expr? code)
        | Assert(expr test, expr? msg)
        | SubroutineCall(symbol name, symbol? original_name, call_arg* args, expr? dt)
        | Where(expr test, stmt* body, stmt* orelse)
        | WhileLoop(expr test, stmt* body)
        | Nullify(symbol* vars)
        | Flush(int label, expr unit, expr? err, expr? iomsg, expr? iostat)
        | ListAppend(expr a, expr ele)
        | AssociateBlockCall(symbol m)
        | CPtrToPointer(expr cptr, expr ptr, expr? shape)
        | BlockCall(int label, symbol m)
        | SetInsert(expr a, expr ele)
        | SetRemove(expr a, expr ele)
        | ListInsert(expr a, expr pos, expr ele)
        | ListRemove(expr a, expr ele)
        | ListClear(expr a)
        | DictInsert(expr a, expr key, expr value)
    
    
    expr
        = IfExp(expr test, expr body, expr orelse, ttype type, expr? value)
            -- Such as: (x, y+z), (3.0, 2.0) generally not known at compile time
        | ComplexConstructor(expr re, expr im, ttype type, expr? value)
        | NamedExpr(expr target, expr value, ttype type)
        | FunctionCall(symbol name, symbol? original_name,
                call_arg* args, ttype type, expr? value, expr? dt)
        | DerivedTypeConstructor(symbol dt_sym, expr* args, ttype type, expr? value)
        | EnumTypeConstructor(symbol dt_sym, expr* args, ttype type, expr? value)
        | ImpliedDoLoop(expr* values, expr var, expr start, expr end,
                        expr? increment, ttype type, expr? value)
        | IntegerConstant(int n, ttype type)
        | IntegerBOZ(int v, integerboz intboz_type, ttype? type)
        | IntegerBitNot(expr arg, ttype type, expr? value)
        | IntegerUnaryMinus(expr arg, ttype type, expr? value)
        | IntegerCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | IntegerBinOp(expr left, binop op, expr right, ttype type, expr? value)
        | RealConstant(float r, ttype type)
        | RealUnaryMinus(expr arg, ttype type, expr? value)
        | RealCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | RealBinOp(expr left, binop op, expr right, ttype type, expr? value)
        | ComplexConstant(float re, float im, ttype type)
        | ComplexUnaryMinus(expr arg, ttype type, expr? value)
        | ComplexCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | ComplexBinOp(expr left, binop op, expr right, ttype type, expr? value)
        | LogicalConstant(bool value, ttype type)
        | LogicalNot(expr arg, ttype type, expr? value)
        | LogicalCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | LogicalBinOp(expr left, logicalbinop op, expr right, ttype type, expr? value)
        | TemplateBinOp(expr left, binop op, expr right, ttype type, expr? value)
    
        | ListConstant(expr* args, ttype type)
        | ListLen(expr arg, ttype type, expr? value)
        | ListConcat(expr left, expr right, ttype type, expr? value)
    
        | SetConstant(expr* elements, ttype type)
        | SetLen(expr arg, ttype type, expr? value)
    
        | TupleConstant(expr* elements, ttype type)
        | TupleLen(expr arg, ttype type, expr value)
    
        | StringConstant(string s, ttype type)
        | StringConcat(expr left, expr right, ttype type, expr? value)
        | StringRepeat(expr left, expr right, ttype type, expr? value)
        | StringLen(expr arg, ttype type, expr? value)
        | StringItem(expr arg, expr idx, ttype type, expr? value)
        | StringSection(expr arg, expr? start, expr? end, expr? step, ttype type, expr? value)
        | StringCompare(expr left, cmpop op, expr right, ttype type, expr? value)
        | StringOrd(expr arg, ttype type, expr? value)
        | StringChr(expr arg, ttype type, expr? value)
    
        | DictConstant(expr* keys, expr* values, ttype type)
        | DictLen(expr arg, ttype type, expr? value)
    
        | Var(symbol v)
    
        | ArrayConstant(expr* args, ttype type)
        | ArrayItem(expr v, array_index* args, ttype type, expr? value)
        | ArraySection(expr v, array_index* args, ttype type, expr? value)
        | ArraySize(expr v, expr? dim, ttype type, expr? value)
        | ArrayBound(expr v, expr? dim, ttype type, arraybound bound,
                     expr? value)
        | ArrayTranspose(expr matrix, ttype type, expr? value)
        | ArrayMatMul(expr matrix_a, expr matrix_b, ttype type, expr? value)
        | ArrayPack(expr array, expr mask, expr? vector, ttype type, expr? value)
        | ArrayReshape(expr array, expr shape, ttype type, expr? value)
    
        | BitCast(expr source, expr mold, expr? size, ttype type, expr? value)
        | DerivedRef(expr v, symbol m, ttype type, expr? value)
        | EnumRef(symbol v, symbol? m, string property, ttype type, expr? value)
        | OverloadedCompare(expr left, cmpop op, expr right, ttype type, expr? value, expr overloaded)
        | OverloadedBinOp(expr left, binop op, expr right, ttype type, expr? value, expr overloaded)
        | Cast(expr arg, cast_kind kind, ttype type, expr? value)
        | ComplexRe(expr arg, ttype type, expr? value)
        | ComplexIm(expr arg, ttype type, expr? value)
        | DictItem(expr a, expr key, expr? default, ttype type, expr? value)
        | CLoc(expr arg, ttype type, expr? value)
        | PointerToCPtr(expr arg, ttype type, expr? value)
        | GetPointer(expr arg, ttype type, expr? value)
        | ListItem(expr a, expr pos, ttype type, expr? value)
        | TupleItem(expr a, expr pos, ttype type, expr? value)
        | ListSection(expr a, array_index section, ttype type, expr? value)
        | ListPop(expr a, expr? index, ttype type, expr? value)
        | DictPop(expr a, expr key, ttype type, expr? value)
        | SetPop(expr a, ttype type, expr? value)
        | IntegerBitLen(expr a, ttype type, expr? value)
    
    
    -- `len` in Character:
    -- >=0 ... the length of the string, known at compile time
    --  -1 ... character(*), i.e., inferred at runtime
    --  -2 ... character(:), allocatable (possibly we might use -1 for that also)
    --  -3 ... character(n+3), i.e., a runtime expression stored in `len_expr`
    
    -- kind: The `kind` member selects the kind of a given type. We currently
    -- support the following:
    -- Integer kinds: 1 (i8), 2 (i16), 4 (i32), 8 (i64)
    -- Real kinds: 4 (f32), 8 (f64)
    -- Complex kinds: 4 (c32), 8 (c64)
    -- Character kinds: 1 (utf8 string)
    -- Logical kinds: 1, 2, 4: (boolean represented by 1, 2, 4 bytes; the default
    --     kind is 4, just like the default integer kind, consistent with Python
    --     and Fortran: in Python \"Booleans in Python are implemented as a subclass
    --     of integers\", in Fortran the \"default logical kind has the same storage
    --     size as the default integer\"; we currently use kind=4 as default
    --     integer, so we also use kind=4 for the default logical.)
    
    ttype
        = Integer(int kind, dimension* dims)
        | Real(int kind, dimension* dims)
        | Complex(int kind, dimension* dims)
        | Character(int kind, int len, expr? len_expr, dimension* dims)
        | Logical(int kind, dimension* dims)
        | Set(ttype type)
        | List(ttype type)
        | Tuple(ttype* type)
        | Derived(symbol derived_type, dimension* dims)
        | Enum(symbol enum_type, dimension *dims)
        | Class(symbol class_type, dimension* dims)
        | Dict(ttype key_type, ttype value_type)
        | Pointer(ttype type)
        | CPtr()
        | TypeParameter(identifier param, dimension* dims, restriction* rt)
    
    restriction = Restriction(trait rt)
    
    trait = SupportsZero | SupportsPlus | Divisible | Any
    
    binop = Add | Sub | Mul | Div | Pow | BitAnd | BitOr | BitXor | BitLShift | BitRShift
    
    logicalbinop = And | Or | Xor | NEqv | Eqv
    
    cmpop = Eq | NotEq | Lt | LtE | Gt | GtE
    
    integerboz = Binary | Hex | Octal
    
    arraybound = LBound | UBound
    
    cast_kind
        = RealToInteger
        | IntegerToReal
        | LogicalToReal
        | RealToReal
        | TemplateToReal
        | IntegerToInteger
        | RealToComplex
        | IntegerToComplex
        | IntegerToLogical
        | RealToLogical
        | CharacterToLogical
        | CharacterToInteger
        | CharacterToList
        | ComplexToLogical
        | ComplexToComplex
        | ComplexToReal
        | LogicalToInteger
        | RealToCharacter
        | IntegerToCharacter
        | LogicalToCharacter
    
    dimension = (expr? start, expr? length)
    
    alloc_arg = (symbol a, dimension* dims)
    
    attribute = Attribute(identifier name, attribute_arg *args)
    
    attribute_arg = (identifier arg)
    
    call_arg = (expr? value)
    
    tbind = Bind(string lang, string name)
    
    array_index = (expr? left, expr? right, expr? step)
    
    do_loop_head = (expr? v, expr? start, expr? end, expr? increment)
    
    case_stmt = CaseStmt(expr* test, stmt* body) | CaseStmt_Range(expr? start, expr? end, stmt* body)
    
    }")
    ```
    
    [result][nextjournal#output#14995343-d18f-4579-b61f-96398c72c557#result]
    
    ## Instaparse Grammar for ASDL
    
    We'll parse the ASDL spec for ASR into Clojure vectors and hashmaps, then generate clojure.specs for terms and forms from the vectors and hashmaps.
    
    The only thing less-than-obvious in the following grammar are angle brackets. They mean "don't bother reporting this term." Cuts down on clutter in the output.
    
    The grammar says:
    
    1. An ASDL spec is a bunch of ***productions*** or ASDL-DEFs
    2. An ASDL-DEF, aka ***speclet***, is a triple of (a) ***term*** or ASDL-TERM, (b) an equals sign, and (c) one or more ASDL-FORMs separated by vertical bar characters. The meaning of an ASDL-DEF is an *alternation*, a list of alternative ASDL-FORMs. 
    3. There are three *kinds* of ASDL-FORM or speclet: a ***composite***, a ***symconst***, or a ***tuple***. 
    4. A *composite* is a ASDL-HEAD ***head*** followed by ASDL-ARGSs args. Args are identical in shape to a tuple. 
    5. A *symconst* is just an identifier, reckoned as the *head* of the symconst. 
    6. A tuple is a comma-separated list (in round brackets) of pairs of ***type*** and ***variable***.
    
        A tuple is anonymous, but we gensym a *head* for them, so that every kind of ASDL-FORM has a head, for convenience.
    7. Types can have *quantitative qualifiers*, aka *multiplicities*: STAR or QUES, meaning that the variable denotes "zero or more" and "at least one" instance of the type respectively. The default quantity is "exactly once."
    
    The big picture to remember about *terms* and *heads* is that a *speclet* looks like one of the following three:
    
    1. `term` `=` `composite-`*`head`*`-1` `args` `|` `composite-`*`head`*`-2` `args` `|` ...
    2. `term` `=` `symconst-`*`head`* `|` `symconst-`*`head`* `|` ...
    3. `term` `=` `tuple` (anonymous \[gensymmed\] *head*) 
    
    A *term* corresponds to one or more (a *bunch* of) *heads*, but each head corresponds to exactly one term. 
    
    A term has exactly one *speclet*. The speclet is the whole line, left-hand side (term) and right-hand side (bunch of *forms*, one per head). 
    
    All forms in a speclet have the same kind, composite, symconst, or tuple. There won't be a mixture of coposites and speclets, for instance, on the right-hand side of any term.
    
    In addition to the 3 kinds, it turns out there are (at one count) 28 terms and speclets, and 227 heads, forms, and clojure.specs when we're done. The number grows slowly as we add features to AS.
    
    ```clojure id=029fe8f0-78f1-4cf8-8271-807e090e83a4
    (def asdl-grammar "
       MODULE         = SPC* <'module'> SPC* IDENT LBRACE SPEC RBRACE
       SPEC           = (ASDL-DEF SPC*)*
    (* **************************************************************** *)
      <SPC>           = <#'\\s*(--[^\\n]*)?'> (* eat comments quickly * *)
      <BAR>           = <SPC* '|' SPC*>
      <COMMA>         = <SPC* ',' SPC*>
       STAR           = <SPC* '*' SPC*>
       QUES           = <SPC* '?' SPC*>
      <EQ>            = <SPC* '=' SPC*>
      <LBRACE>        = <SPC* '{' SPC*>
      <RBRACE>        = <SPC* '}' SPC*>
      <LPAR>          = <SPC* '(' SPC*>
      <RPAR>          = <SPC* ')' SPC*>
      <IDENT>         = #'[A-Za-z_][A-Za-z0-9_\\.\\-]*'
    (* **************************************************************** *)
       ASDL-DEF       = ASDL-TERM EQ ASDL-FORMS  (* aka 'speclet' ***** *)
       ASDL-TERM      = IDENT
       ASDL-FORMS     = ASDL-FORM (BAR ASDL-FORM)*
      <ASDL-FORM>     = ASDL-COMPOSITE
                      | ASDL-SYMCONST
                      | ASDL-TUPLE
      
       ASDL-COMPOSITE = ASDL-HEAD ASDL-ARGS
       ASDL-SYMCONST  = IDENT
       ASDL-TUPLE     = ASDL-ARGS
    
       ASDL-HEAD      = IDENT
       ASDL-ARGS      = LPAR ASDL-DECL (COMMA ASDL-DECL)* RPAR
                      | LPAR RPAR
       ASDL-DECL      = ASDL-TYPE SPC* ASDL-NYM
       ASDL-TYPE      = IDENT | IDENT STAR | IDENT QUES
       ASDL-NYM       = IDENT
      ")
    (def asdl-parser (insta/parser asdl-grammar))
    nil  ;; Stanch big output.
    ```
    
    Capture the parse of ASR.asdl into hiccup format **(**<https://github.com/weavejester/hiccup>**).** 
    
    ```clojure id=28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d
    (def asr-pre-spec (asdl-parser all-asr))
    ```
    
    [result][nextjournal#output#28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d#result]
    
    ## Raw Hiccup for all Speclets
    
    Strip off the `module` info, leaving only ASDL-DEFs, i.e., *speclets*. 
    
    ```clojure id=ef06350e-bcee-4e53-ac1f-d9975ed18fc6
    (def speclets
      (vec (rest
             ((-> (zip/vector-zip asr-pre-spec)
                zip/down zip/right zip/right) 0))))
    ```
    
    [result][nextjournal#output#ef06350e-bcee-4e53-ac1f-d9975ed18fc6#result]
    
    ## Hashmap from Speclet
    
    This isn't literate programming, so I can't show you "what we're doing" before I show you "how we do it." But at least I can *tell* you "what we're doing:" we need a function to produce a Clojure hash-map from any speclet, i.e., any ASDL-DEF: its ASDL-TERM and all its ASDL-FORMs
    
    ## Helpers
    
    ### Shallow Hashmap from Speclet
    
    Step 1: Convert the top level of one speclet to a hashmap:
    
    ```clojure id=0a784b7a-e707-41fa-8598-d4a4586c77c6
    (defn shallow-map-from-speclet
      "Convert an ASDL-DEF into a map from :ASDL-TERM to the name of 
      the speclet and from :ASDL-FORMS into a list of alternative forms."
      [speclet]
      (let [[sign asdl-term asdl-forms] speclet
            _ (assert (= sign :ASDL-DEF))  ;; TODO: replace with s/fspec
            [sign & forms] asdl-forms  ;; listify forms
            _ (assert (= sign :ASDL-FORMS))
            renested [asdl-term [:ASDL-FORMS forms]]
            denested (mapcat identity renested)]
        (apply hash-map denested)))
    (pp (shallow-map-from-speclet (speclets 3)))  ;; symconst unit test
    (pp (shallow-map-from-speclet (speclets 0)))  ;; composite unit test
    (pp (shallow-map-from-speclet (speclets 22))) ;; tuple unit tes
    ```
    
    ### Decl Hashmap
    
    Step 2: Convert a single ASDL-DECL, which is either the right-hand side of an ASDL-TUPLE or the argument list of an ASDL-COMPOSITE, into a hashmap:
    
    ```clojure id=4fb2c34f-9857-4ec8-bdea-f6776d3093c1
    (defn decl-map
        "Convert [:ASDL-DECL [:ASDL-TYPE ...] [:ASDL-NYM ...]]
        into {:ASDL-TYPE ..., :MULTIPLICITY ..., :ASDL-NYM ...}.
        TODO: Rewrite argument validation with s/fdef."
        [decl-hiccup]
        (let [_ (assert (= (decl-hiccup 0) :ASDL-DECL))
              [sign type-nym & opt] (decl-hiccup 1)
              _ (assert (= sign :ASDL-TYPE))
              [sign decl-nym] (decl-hiccup 2)
              _ (assert (= sign :ASDL-NYM))]
          {:ASDL-TYPE type-nym
           :MULTIPLICITY (case opt
                           (([:STAR])) ::zero-or-more
                           (([:QUES])) ::at-most-once
                           ::once)  ;; default
           :ASDL-NYM decl-nym}))
    ```
    
    ### ASDL Form
    
    Step 3: Convert each of the three kinds of ASDL-FORM --- symconsts, composites, and tuples --- to a hashmap.
    
    All tuples get a unique, gensymmed namespaced-keyword name for a *head*.
    
    ```clojure id=6a635fa0-719a-4eb6-9698-1ed0488244f7
    (defmulti asdl-form first)
    (defmethod asdl-form :ASDL-SYMCONST [form]
      (apply hash-map form))
    (defmethod asdl-form :ASDL-COMPOSITE [form]
      (let [[_ head args-pre] form
            [_ & decls] args-pre]  ;; & means listify
        {:ASDL-COMPOSITE {:ASDL-HEAD (second head)
                          :ASDL-ARGS (map decl-map decls)}}))
    (defmethod asdl-form :ASDL-TUPLE [form]
      (let [[_ args-pre] form
            [_ & decls] args-pre] ;; & means listify
        {:ASDL-TUPLE (name (gensym "asr-tuple"))
         :ASDL-ARGS (map decl-map decls)}))
    ;;; unit test
    (pp (->> (shallow-map-from-speclet (speclets 22))
          :ASDL-FORMS
          (map asdl-form)))
    ```
    
    ## Hashmap from Speclet, Itself
    
    One entire speclet to a hashmap:
    
    ```clojure id=711cc44d-616c-4d69-a01e-5138898ee4e2
    (defn hashmap-from-speclet [speclet]
      (let [pre (shallow-map-from-speclet speclet)
            term (:ASDL-TERM pre)
            forms (map asdl-form (:ASDL-FORMS pre))]
        {:ASDL-TERM term
         :ASDL-FORMS forms}))
    (pp (hashmap-from-speclet (speclets 0)))  
    (pp (hashmap-from-speclet (speclets 3)))
    (pp (hashmap-from-speclet (speclets 22)))
    ```
    
    # Big Map of Speclets From Terms
    
    Example: term `::symbol` maps to `::Function`, `::Program`, `::Module`, and more.
    
    Except for `SymbolTable`, which is not written, terms are in `snake_case`.
    
    Have fun clicking around the large output of this cell. There are about 28 terms with about 227 heads.
    
    ```clojure id=68960eae-8344-4331-a419-cea794ee5480
    (defn map-pair-from-speclet-map [speclet-map]
      [(keyword "asr" (:ASDL-TERM speclet-map))  ;; no kebab'bing
       (:ASDL-FORMS speclet-map)])
    (def big-map-of-speclets-from-terms
      ;; TODO: Make some nice swiss arrows to do all this.
      (apply hash-map
        (mapcat identity  ;; flatten one level
          (map
            (comp map-pair-from-speclet-map
              hashmap-from-speclet)
            speclets))))
    ```
    
    [result][nextjournal#output#68960eae-8344-4331-a419-cea794ee5480#result]
    
    # Big List of Stuff
    
    A ***stuff*** is a map of `:head`, `:term`, `:kind`, and `:form` for the approximately 227 heads & forms of ASR. A stuff is all we need for making clojure.specs from terms, heads, & forms. The stuff keywords `:head`, `:term`, `:kind`, and `:form` need not be namespaced.
    
    This  big list of stuff is like a big, flat, denormalized database table.
    
    ## Generalized Heads
    
    For composites, the "head" is obvious because it's a symbol followed by an args tuple.
    
    For symconsts, the "heads" are just the symbolic constants themselves.
    
    For all tuples, the head is gensymmed. Example: head `::asr-tuple3805` (kebab-case; exception to the rule for heads), corresponds to term `::alloc_arg`, in snake case, like all terms.
    
    ### Don't Kebab Too Early
    
    Heads, except for gensymmed heads for tuples, are in PascalCase; don't kebab them. We'll kebab the derived namespaced keywords for naming clojure.specs.
    
    ## Helper: Stuff from Term & Form
    
    Here we go again, illiterates! Gotta show you how we're doing it before showing you what we're doing!
    
    The intention is to partially evaluate `stuff-from-term-form` on a term, then map the result over all the forms for that term.
    
    ```clojure id=eaa857a3-9d94-414f-9394-54acd01bf557
    (defn kind-from-form [form]
      (-> form first first))
    (defn head-from-kind-form [kind form]
      (case kind
        :ASDL-COMPOSITE (-> form first second :ASDL-HEAD)
        :ASDL-SYMCONST (-> form first second) ;; symconst itself
        :ASDL-TUPLE (-> form first second)))
    (defn stuff-from-term-form [term form]
      (let [kind (-> form kind-from-form)
            ghead (head-from-kind-form kind form)
            kwh (keyword "asr" ghead)] ;; no kebab'bing
        {:head kwh,:term term,:kind kind,:form,form}))
    ```
    
    ```clojure id=6a754b5e-24be-4d05-88c5-e653c5ce4bad
    (def big-list-of-stuff
      (mapcat identity
        (map (fn [speclet]
             (let [[term forms] speclet
                   htkfs (map (partial stuff-from-term-form term) forms)]
               htkfs))
        big-map-of-speclets-from-terms)))
    ```
    
    [result][nextjournal#output#6a754b5e-24be-4d05-88c5-e653c5ce4bad#result]
    
    # All Symconst Specs
    
    Clojure.specs for symconsts are easiest because they don't depend on other clojure.specs. There are about 72 symconsts (more as ASR grows):
    
    ## Symconst Stuffs
    
    ```clojure id=abc8ee32-b0fe-469c-8c04-c70c3f2c569e
    (def symconst-stuffs
       (filter #(= (:kind %) :ASDL-SYMCONST) big-list-of-stuff))
    ```
    
    [result][nextjournal#output#abc8ee32-b0fe-469c-8c04-c70c3f2c569e#result]
    
    ## Symconst-Head-Specs
    
    This next code block INSTALLS the (about) 72 head-specs by `eval`'ing the `s/defs` written by `` `(s/def ...) ``. A spec is *installed* into a hidden Clojure Spec Registry by side-effect and is associated with the namespaced keyword produced by `nskw-kebab-from`. Once this next code block runs, we'll have (about) 72 head-specs magically installed and we can refer to them by namespaced kebab'bed keyword name. For example, `::implementation` will be installed and we can refer to it via `(s/spec ::implementation)`. 
    
    All specs, head-specs and term-specs alike must be installed before being referred-to. Later, we'll break co-recursive cycles by installing defective specs then backpatching them. For example, the term-spec for `::symbol` refers to the term-spec for `::symbol-table`, which refers to the term-spec for `::symbol`. Clojure.spec can't tolerate that, but it can tolerate a defective termsspec for `::symbol-table` that we backpatch later. 
    
    Construct and install all (approximately) 72 symconst head-specs:
    
    ```clojure id=82c3d607-5487-439b-9a69-2f18e938929b
    (defn spec-from-symconst-stuff [symconst-stuff]
      (let [symconst (-> symconst-stuff :form :ASDL-SYMCONST)
            nskw (nskw-kebab-from symconst)]
        `(s/def ~nskw #{(quote ~(symbol symconst))})))
    ;; side-effecting code: The value of this expression is
    ;; only for inspection.
    (->> symconst-stuffs
      (map spec-from-symconst-stuff)
      (map eval))  ;; SIDE-EFFECT! Install! Woo Hoo!
    ```
    
    [result][nextjournal#output#82c3d607-5487-439b-9a69-2f18e938929b#result]
    
    ### Unit Tests
    
    We see that each of the 72 head-specs is just a predicate for an unqualified symbol. The unqualified symbol `'Add` conforms to the head-spec `::add` in the `asr` namespace.
    
    ```clojure id=f1b41768-cc74-4d27-a958-78929defb755
    (s/conform (s/spec ::add) 'Add)
    ```
    
    Also, enjoy your first taste of a generator, trivial in this case, but instructive:
    
    ```clojure id=7dd2b67e-352d-400a-9de0-087202a0e907
    (gen/generate (s/gen ::add))
    ```
    
    ## Symconst-Term-Specs
    
    To check an instance or utterance of ASR like expr-221000, we'll need to check its sub-parts by term, not by head.
    
    ### Symconst Stuffss \[sic\] by Term
    
    First, partition the symconst specs by term. There are about 13 terms categorizing the (approx) 72 symconst heads.
    
    ```clojure id=dfae2600-bc53-44b4-a97f-c3758c2b85cd
    (def symconst-stuffss-by-term (partition-by :term symconst-stuffs))
    ```
    
    [result][nextjournal#output#dfae2600-bc53-44b4-a97f-c3758c2b85cd#result]
    
    ### Symconst Spec for Term \[sic\]
    
    For each term, write a `set` containing its alternative heads, e.g., the term `binop` is one of the ten heads `Add`, `Sub`, and so on, to `BitRShift`.
    
    To unit-test `spec-for-term`, `eval` one of them and check it:
    
    ```clojure id=73cb5487-9c13-42b4-a8ad-e5548ba2942b
    (defn symconst-spec-for-term [stuffs-for-term]
      (let [term (-> stuffs-for-term first :term) ;; same for all! TODO: assert
            term-nskw (nskw-kebab-from (name term))
            ss1
            (->> stuffs-for-term
              (map (fn [stuff]
                     (let [head (head-from-kind-form (:kind stuff) (:form stuff))]
                       (-> head symbol)))))]
        `(s/def ~term-nskw (set (quote ~ss1)))))  ;; Here is the 'set'!
    (def utest-symconst-term-spec
      (-> (nth symconst-stuffss-by-term 3)
        symconst-spec-for-term
        #_echo
        eval))
    (s/explain utest-symconst-term-spec 'Add)
    #_(s/exercise ::binop)  ;; every time you run you get different results
    ```
    
    ### Install
    
    To install the thirteen term-specs for symconsts, `eval` them.
    
    ```clojure id=60580897-7d67-4123-b709-e0dc94fc6961
    (->> symconst-stuffss-by-term
      (map symconst-spec-for-term)
      (map eval)) ;; SIDE-EFFECT! Woo Hoo!
    ```
    
    ### Unit Test
    
    ```clojure id=bfe11b21-7e69-4d77-9a47-6b70b7024d87
    (s/exercise ::trait)
    ```
    
    # Tuple Specs
    
    What do we want to see for a tuple head-spec? How about an `s/cat`?
    
    There are six tuple heads. Their names will change from run-to-run because the names are gensymmed.
    
    ```clojure id=5cf06789-ece6-4a36-9c6c-c22861604342
    (def tuple-stuffs
      (filter #(= (:kind %) :ASDL-TUPLE)
        big-list-of-stuff))
    ```
    
    [result][nextjournal#output#5cf06789-ece6-4a36-9c6c-c22861604342#result]
    
    We won't be able to test these until we have specs for *identifier*, *expr*, *symbol*, and *dimension.* Except for *identifier*, which isn't in ASR.asdl, we'll stub them now and backpatch them later.
    
    ## Spec for *identifier*
    
    We can't use just `symbol?` because it generates namespaced symbols, and they aren't useful for testing LPython. We'll need a custom generator (<https://clojure.org/guides/spec#_custom_generators>). 
    
    The following attempt has performance problems and will be discarded. We save it as a lesson in this kind of dead end.
    
    ```clojure id=a57ea154-1d58-4179-a401-bb061109363e
    (def identifier-re #"[a-zA-Z_][a-zA-Z0-9_]*")
    (s/def ::identifier
      (s/with-gen
        symbol?
        (fn [] (gen/such-that #(re-matches identifier-re (name %)) (gen/symbol)))))
    #_(s/exercise ::identifier 100) 
    ```
    
    We must, sadly, eliminate the solution above because it occasionally fails the *such-that*. Explore via exercising the candidate spec, say, 100 times (uncomment the expression above and evaluate the cell). 
    
    Here is a better solution that, sadly but harmlessly, lacks underscores.
    
    ```clojure id=0989a589-afd2-4f99-9ee6-cfe5671beeea
    (let [alpha-re #"[a-zA-Z]"  ;; The famous "let over lambda."
          alphameric-re #"[a-zA-Z0-9]*"]
      (def alpha?
        #(re-matches alpha-re %))
      (def alphameric?
        #(re-matches alphameric-re %))
      (defn identifier? [s]
        (and (alpha? (subs s 0 1))
          (alphameric? (subs s 1))))
      (def identifier-generator
        (tgen/let [c (gen/char-alpha)
                   s (gen/string-alphanumeric)]
          (str c s)))
      (s/def ::identifier  ;; side effects the spec registry!
        (s/with-gen
          identifier?
          (fn [] identifier-generator))))
    
    (s/exercise ::identifier #_100)
    ```
    
    ## Tuple-Term-Spec Stubs for *Expr*, *Symbol*, *Dimension*
    
    Exprs and symbols are composites, so we can expose a pattern for stub term-specs from these two. We'll choose a list with one of the valid head and zero or more randomly generated identifiers.
    
    ```clojure id=62d1bc11-9f80-4f51-a486-bafe26fa657c
    (defn heads-for-composite [term]
      (->> (term big-map-of-speclets-from-terms)
        (map :ASDL-COMPOSITE)
        (map :ASDL-HEAD)
        (map symbol)
        set))
    
    (defn generator-for-heads [heads]
      (tgen/let [head (s/gen heads)
                 rest (gen/list (s/gen ::identifier))]
        (cons head rest)))
    
    (defn lpred [heads]
      (s/and seq?
        (fn [lyst] (-> lyst count (>= 1)))
        (fn [lyst] (-> lyst first heads))))
    
    ;; The following doesn't work for unknown reason. 
    ;; Fails spec for 'let' when eval'ed. Some subtlety 
    ;; of the macrology of 'let.' Punt, but retain for
    ;; sake of instruction and TODO.
    #_(defn write-stub-spec-for-composite [term]
        `(let [heads (heads-for-composite ~term)]
         (s/def ~term
           (s/with-gen
             (lpred heads)
             (fn [] (generator-for-heads heads))))))
    
    #_(def symbol-stub-spec (write-stub-spec-for-composite ::symbol)) 
    #_(eval symbol-stub-spec)  ;; fails spec for 'let'
    
    ;; Would like to abstract the common pattern of the 
    ;; following two cases, but can't easily. See above.
    (let [heads (heads-for-composite ::symbol)]
      (s/def ::symbol
          (s/with-gen
            (lpred heads)
            (fn [] (generator-for-heads heads)))))
    
    (let [heads (heads-for-composite ::expr)]
      (s/def ::expr
          (s/with-gen
            (lpred heads)
            (fn [] (generator-for-heads heads)))))
    
    (s/exercise ::expr #_100) 
    ```
    
    A dimension is, itself, a tuple, so we'll have a weak stub spec at first.
    
    ```clojure id=5df0afae-c1df-41f8-bcbd-de4f36275c14
    (s/def ::dimension list?)
    ```
    
    ### Spec Fragment from Arg, Args
    
    Illiterates of the world, unite! Here is some "how-to" before the "what-for."
    
    Convert multiplicities into clojure.spec equivalents;
    
    ```clojure id=61909e52-e156-497c-b97b-cff0cda6c51f
    (defn spec-from-arg [arg]
      (let [type (nskw-kebab-from (:ASDL-TYPE arg))
            nym (:ASDL-NYM arg)]
        (case (:MULTIPLICITY arg)
          ::once `(s/spec ~type)
          ::at-most-once `(s/? (s/spec ~type))
          ::zero-or-more `(s/* (s/spec ~type)))))
    ```
    
    Just map over that:
    
    ```clojure id=91c30964-89f5-4cdf-89a1-b85f04cb17cb
    (defn spec-from-args [args]
      (let [nyms (->> args (map :ASDL-NYM) #_echo)
            kyms (->> nyms (map (comp keyword name)) #_echo)
            specules (->> args (map spec-from-arg) #_echo)
            riffle (-> (interleave kyms specules) #_echo)]
        `(s/cat ~@riffle)))
    ```
    
    ## Install Tuple-Head-Specs
    
    Notice the bang (`!`) on the end of the name of `spec-from-tuple-stuff!`. It doesn't really, itself, side-effect the Spec Registry, but its only use is to side-effect the Registry, so why not name it so?
    
    ```clojure id=7f5fca15-06d1-46d2-936b-50b766b11b83
    (defn spec-from-tuple-stuff! [tuple-stuff]
      (let [nskw (nskw-kebab-from (name (:head tuple-stuff)))
            args (-> tuple-stuff :form :ASDL-ARGS)]
        `(s/def ~nskw ~(spec-from-args args))))  ;; side effect!
    (->> tuple-stuffs
      (map spec-from-tuple-stuff!)
      echo
      (map eval))  ;; SIDE-EFFECT Woo Hoo! Bang Bang!
    ```
    
    ### Unit Tests
    
    You may have to modify these by hand because the gensyms may change every run:
    
    ```clojure id=76042bc7-a3f9-4605-82a5-1cec58263f6f
    (s/conform ::asr-tuple-3805 '((a b c) (f g h)))
    ```
    
    ```clojure id=586a8c8f-d821-496e-af7d-85451363eaa1
    (gen/generate (s/gen ::asr-tuple-3805))
    ```
    
    ## Tuple Term-Specs
    
    As before, we really need clojure.specs for the terms corresponding to the heads.
    
    ### Tuple Stuffss \[sic\] by Term
    
    ```clojure id=0ecf68b0-b6ca-4771-962d-969eaf239ce6
    (def tuple-stuffss-by-term (partition-by :term tuple-stuffs))
    ```
    
    [result][nextjournal#output#0ecf68b0-b6ca-4771-962d-969eaf239ce6#result]
    
    ### Tuple-Term-Spec
    
    ```clojure id=aae20034-2697-43c1-8f9f-c8a52c836b30
    (defn tuple-spec-for-term [stuffs]
      (let [term (-> stuffs first :term)
            term-nskw (nskw-kebab-from (name term))
            head (-> stuffs first :head name nskw-kebab-from)]
        `(s/def ~term-nskw (s/spec ~head))))
    ```
    
    ### Install
    
    To install the 6 term-specs, `eval` them.
    
    ```clojure id=af6218fc-c359-4faf-b8ee-da7b5e2a5f18
    (->> tuple-stuffss-by-term
      (map tuple-spec-for-term)
      (map eval))  ;; SIDE-EFFECT! Woo Hoo!
    ```
    
    ```clojure id=22532e4d-0b45-479a-b282-af17deef6a52
    (s/exercise ::dimension)
    ```
    
    [result][nextjournal#output#22532e4d-0b45-479a-b282-af17deef6a52#result]
    
    # Hand-Written Term Spec for SymbolTable
    
    ASDL doesn't offer an easy way to specify maps, but Clojure.spec does. ASR.asdl doesn't have a spec for `SymbolTable`, so we write one by hand and upgrade it as we go along. 
    
    We cannot define this spec until we define the others because `(s/spec ::symbol)` doesn't exist yet. We'll backpatch it later
    
    ```clojure id=79dae76d-9e2e-442c-a946-7948c4afae60
    (s/def ::symbol-table
      (s/cat
        :head #(= % 'SymbolTable)
        :unique-id int?
        :symbols (s/map-of keyword?
                   #_#(do % true) 
                   (s/spec ::symbol))))
    ```
    
    ```clojure id=fe81e0bc-24f9-40d3-a555-f4000eb4ab55
    (s/explain ::symbol-table '(SymbolTable 3 {}))
    ```
    
    But it's going to have to improve (also notice we may harmlessly surround the spec-name nskw in a call of `s/spec`):
    
    Let's check a real symbol table
    
    ```clojure id=83346640-b369-4d5b-8698-5ce6ea21cdd1
    (->> user/expr-01-211000 second echo (s/explain ::symbol-table))
    ```
    
    # Backpatching Symbol
    
    TODO
    
    # First Composite Spec: `TranslationUnit`
    
    We write specs as data lists and `eval` them later. Turns out it's necessary to do that, and it's a beneficial accident lest we clutter up the namespace of specs.
    
    As usual, because this is illiterate programming, we must define things before we can use them. Read the code backwards to get the big picture.
    
    Composites and tuples have lists of type-var pairs, that is, of args. We've already handled arg lists by defining `spec-from-args` above. 
    
    Specs for all tuples' heads and terms have already been installed.
    
    Specs for all symconsts' heads and terms have already been installed.
    
    ## Composite Head-Specs
    
    Composites have a head and a possibly empty list of args.
    
    ```clojure id=cabc5d67-ea28-4d57-8559-38c4a981c83e
    (defn spec-from-composite [composite]
      (let [head (-> composite :ASDL-HEAD symbol)
            nskw (-> head nskw-kebab-from #_echo)
            args (-> composite :ASDL-ARGS)]
        `(s/def ~nskw ~(spec-from-args args))))
    ```
    
    # TODO
    
    Automate the transformation of ASR instances from colon-following to colon-preceding form.
    
    [nextjournal#output#9be7df63-a594-451e-bc67-495cf6c8b55d#result]:
    <https://nextjournal.com/data/QmauZQqRJ6yJzhbbij6wzwPXsq4P5bPfk2m8ppddU1VhN1?content-type=application/transit%2Bjson&node-id=9be7df63-a594-451e-bc67-495cf6c8b55d&node-kind=output>
    
    [nextjournal#output#db3884f0-fd65-4f9d-9341-918c9e4733cd#result]:
    <https://nextjournal.com/data/QmTs3sSkGvToXgKLNFKLM9CNdoFe8fyyGJTTuuJWp1cy1A?content-type=application/transit%2Bjson&node-id=db3884f0-fd65-4f9d-9341-918c9e4733cd&node-kind=output>
    
    [nextjournal#output#cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f#result]:
    <https://nextjournal.com/data/QmX5ZSM5Snutx74is877viS1C4KSiMqWE3QvpcgGVtjtNU?content-type=application/transit%2Bjson&node-id=cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f&node-kind=output>
    
    [nextjournal#output#14995343-d18f-4579-b61f-96398c72c557#result]:
    <https://nextjournal.com/data/QmTa8u68FZ9WFKPTxq2JXYmJqawtdCUF2sNomp2ouZk5PC?content-type=application/transit%2Bjson&node-id=14995343-d18f-4579-b61f-96398c72c557&node-kind=output>
    
    [nextjournal#output#28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d#result]:
    <https://nextjournal.com/data/QmNhPv6rPt5dg2Lj9tEayy6gGTm2LsvABtCj321Wb6yHm5?content-type=application/transit%2Bjson&node-id=28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d&node-kind=output>
    
    [nextjournal#output#ef06350e-bcee-4e53-ac1f-d9975ed18fc6#result]:
    <https://nextjournal.com/data/QmTrvCgyJ2eAoxL7ApjGCMLKPePV5j7dyDGHiebPrigtcF?content-type=application/transit%2Bjson&node-id=ef06350e-bcee-4e53-ac1f-d9975ed18fc6&node-kind=output>
    
    [nextjournal#output#68960eae-8344-4331-a419-cea794ee5480#result]:
    <https://nextjournal.com/data/QmTTktsGAbhyw4PVFJQXKEEozMRj2hu51xLGfZbWLxVwsC?content-type=application/transit%2Bjson&node-id=68960eae-8344-4331-a419-cea794ee5480&node-kind=output>
    
    [nextjournal#output#6a754b5e-24be-4d05-88c5-e653c5ce4bad#result]:
    <https://nextjournal.com/data/QmYfBGcSAuBHvWK7b6U3wHv6RNPfjou2uQ5RfpjuB791Fr?content-type=application/transit%2Bjson&node-id=6a754b5e-24be-4d05-88c5-e653c5ce4bad&node-kind=output>
    
    [nextjournal#output#abc8ee32-b0fe-469c-8c04-c70c3f2c569e#result]:
    <https://nextjournal.com/data/QmNRAMYoSiNxpg7CRmfF6wNgh24uxiyBK6S6UWsPMLM6NE?content-type=application/transit%2Bjson&node-id=abc8ee32-b0fe-469c-8c04-c70c3f2c569e&node-kind=output>
    
    [nextjournal#output#82c3d607-5487-439b-9a69-2f18e938929b#result]:
    <https://nextjournal.com/data/QmPXpgYXAUsRNRFbuabAF7y3MrtvPVQk5RJWwnJj3LeSi5?content-type=application/transit%2Bjson&node-id=82c3d607-5487-439b-9a69-2f18e938929b&node-kind=output>
    
    [nextjournal#output#dfae2600-bc53-44b4-a97f-c3758c2b85cd#result]:
    <https://nextjournal.com/data/Qma13YzbSMCLgddf4FJCacHMrudTrwr64CNb3q7jxXkrGM?content-type=application/transit%2Bjson&node-id=dfae2600-bc53-44b4-a97f-c3758c2b85cd&node-kind=output>
    
    [nextjournal#output#5cf06789-ece6-4a36-9c6c-c22861604342#result]:
    <https://nextjournal.com/data/QmTpKxfnoDzZpioE3uSn7L1SnBMkfTb7UD9ofuAnTaFyWm?content-type=application/transit%2Bjson&node-id=5cf06789-ece6-4a36-9c6c-c22861604342&node-kind=output>
    
    [nextjournal#output#0ecf68b0-b6ca-4771-962d-969eaf239ce6#result]:
    <https://nextjournal.com/data/QmWHDTSjPJAWuU4xNhs4QsWuuZBX8W7tFqfAwSFjxiSniT?content-type=application/transit%2Bjson&node-id=0ecf68b0-b6ca-4771-962d-969eaf239ce6&node-kind=output>
    
    [nextjournal#output#22532e4d-0b45-479a-b282-af17deef6a52#result]:
    <https://nextjournal.com/data/QmenvyfpYcvY9ThxAtqBsYMKVKAY3Qd32kUZvkvVf9JxwZ?content-type=application/transit%2Bjson&node-id=22532e4d-0b45-479a-b282-af17deef6a52&node-kind=output>
    
    <details id="com.nextjournal.article">
    <summary>This notebook was exported from <a href="https://nextjournal.com/a/FnEMAE1Pkx2vWFMH6NVpJX?change-id=DF98dM4TZN9i8X5ATYF4Ge">https://nextjournal.com/a/FnEMAE1Pkx2vWFMH6NVpJX?change-id=DF98dM4TZN9i8X5ATYF4Ge</a></summary>
    
    ```edn nextjournal-metadata
    {:article
     {:settings {:numbered? true},
      :nodes
      {"029fe8f0-78f1-4cf8-8271-807e090e83a4"
       {:compute-ref #uuid "bd1eac68-4e49-4cb2-a412-cbdfc0537a7d",
        :exec-duration 516,
        :id "029fe8f0-78f1-4cf8-8271-807e090e83a4",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "0989a589-afd2-4f99-9ee6-cfe5671beeea"
       {:compute-ref #uuid "bbe4315b-df8e-405d-b013-78b813f890be",
        :exec-duration 42,
        :id "0989a589-afd2-4f99-9ee6-cfe5671beeea",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "0a784b7a-e707-41fa-8598-d4a4586c77c6"
       {:compute-ref #uuid "b4af3987-9893-40e3-b892-35818edae6a7",
        :exec-duration 381,
        :id "0a784b7a-e707-41fa-8598-d4a4586c77c6",
        :kind "code",
        :output-log-lines {:stdout 15},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "0ecf68b0-b6ca-4771-962d-969eaf239ce6"
       {:compute-ref #uuid "74dc4d7a-af2c-4113-93ac-2a43ef9f819b",
        :exec-duration 330,
        :id "0ecf68b0-b6ca-4771-962d-969eaf239ce6",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "14995343-d18f-4579-b61f-96398c72c557"
       {:compute-ref #uuid "6f72842d-3d94-42e2-a372-59fa48b284d0",
        :exec-duration 156,
        :id "14995343-d18f-4579-b61f-96398c72c557",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "17507f3b-6ac2-47d1-91e3-260161097282"
       {:compute-ref #uuid "9ae96c51-22ac-4229-9a77-686cffc6d80b",
        :exec-duration 626,
        :id "17507f3b-6ac2-47d1-91e3-260161097282",
        :kind "code",
        :output-log-lines {:stdout 110},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "22532e4d-0b45-479a-b282-af17deef6a52"
       {:compute-ref #uuid "904ea41f-4972-4f2b-b3c9-464e632cc924",
        :exec-duration 413,
        :id "22532e4d-0b45-479a-b282-af17deef6a52",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d"
       {:compute-ref #uuid "7046b19e-567a-4dcb-8a89-64dcbaebb3a2",
        :exec-duration 1997,
        :id "28cdc2c8-4ccd-47c5-8b22-0fef6f5d5f8d",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "29552ba9-d499-4842-9448-63608ce24e24"
       {:environment
        [:environment
         {:article/nextjournal.id
          #uuid "5b45eb52-bad4-413d-9d7f-b2b573a25322",
          :change/nextjournal.id
          #uuid "6140750b-27b0-4b4d-86f3-b07682cd65c6",
          :node/id "0ae15688-6f6a-40e2-a4fa-52d81371f733"}],
        :id "29552ba9-d499-4842-9448-63608ce24e24",
        :kind "runtime",
        :language "clojure",
        :type :prepl,
        :runtime/mounts
        [{:src [:node "ffcf0396-b3f9-40e6-a0c2-654401879781"],
          :dest "/deps.edn"}]},
       "4fb2c34f-9857-4ec8-bdea-f6776d3093c1"
       {:compute-ref #uuid "618e6e8c-ffc2-4c92-95d2-f22e6a6affa7",
        :exec-duration 19,
        :id "4fb2c34f-9857-4ec8-bdea-f6776d3093c1",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "586a8c8f-d821-496e-af7d-85451363eaa1"
       {:compute-ref #uuid "d502154c-52b3-4598-8549-3b56d3be4581",
        :exec-duration 26,
        :id "586a8c8f-d821-496e-af7d-85451363eaa1",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "5cf06789-ece6-4a36-9c6c-c22861604342"
       {:compute-ref #uuid "fb1822f5-1465-4e5d-9cae-5cffd27d5ba8",
        :exec-duration 323,
        :id "5cf06789-ece6-4a36-9c6c-c22861604342",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "5df0afae-c1df-41f8-bcbd-de4f36275c14"
       {:compute-ref #uuid "e4f8cd3a-4191-4fe3-a174-2735582d14a8",
        :exec-duration 8,
        :id "5df0afae-c1df-41f8-bcbd-de4f36275c14",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "60580897-7d67-4123-b709-e0dc94fc6961"
       {:compute-ref #uuid "62b3cca2-51d7-4039-98c9-a09e29494463",
        :exec-duration 13,
        :id "60580897-7d67-4123-b709-e0dc94fc6961",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "60ca7c24-976f-45e5-921f-311004fb1ff4"
       {:compute-ref #uuid "94389b98-1511-43ec-855a-b204eba59342",
        :exec-duration 90,
        :id "60ca7c24-976f-45e5-921f-311004fb1ff4",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "61909e52-e156-497c-b97b-cff0cda6c51f"
       {:compute-ref #uuid "d2afd08a-4b83-4656-945a-4ccb7c1b9a9f",
        :exec-duration 19,
        :id "61909e52-e156-497c-b97b-cff0cda6c51f",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "62d1bc11-9f80-4f51-a486-bafe26fa657c"
       {:compute-ref #uuid "9082caf8-0e30-4e73-ab01-a400d32f38c8",
        :exec-duration 67,
        :id "62d1bc11-9f80-4f51-a486-bafe26fa657c",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "68960eae-8344-4331-a419-cea794ee5480"
       {:compute-ref #uuid "cebe997d-593b-447d-9c59-3c2b53f2be33",
        :exec-duration 451,
        :id "68960eae-8344-4331-a419-cea794ee5480",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "6a635fa0-719a-4eb6-9698-1ed0488244f7"
       {:compute-ref #uuid "c5155cfc-cc05-40ae-a37f-be14eaba1c13",
        :exec-duration 370,
        :id "6a635fa0-719a-4eb6-9698-1ed0488244f7",
        :kind "code",
        :output-log-lines {:stdout 6},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "6a754b5e-24be-4d05-88c5-e653c5ce4bad"
       {:compute-ref #uuid "f7e4b97a-96c4-4940-ab77-1b39c3f0d7fb",
        :exec-duration 414,
        :id "6a754b5e-24be-4d05-88c5-e653c5ce4bad",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "711cc44d-616c-4d69-a01e-5138898ee4e2"
       {:compute-ref #uuid "181576d3-a1eb-453c-8193-e1f05110ab6a",
        :exec-duration 332,
        :id "711cc44d-616c-4d69-a01e-5138898ee4e2",
        :kind "code",
        :output-log-lines {:stdout 21},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "73cb5487-9c13-42b4-a8ad-e5548ba2942b"
       {:compute-ref #uuid "e8794ed2-584e-4b8b-8d3b-d2c0b7a2df31",
        :exec-duration 297,
        :id "73cb5487-9c13-42b4-a8ad-e5548ba2942b",
        :kind "code",
        :output-log-lines {:stdout 2},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "76042bc7-a3f9-4605-82a5-1cec58263f6f"
       {:compute-ref #uuid "88438521-811e-4596-831a-9d99755d4fe6",
        :exec-duration 10,
        :id "76042bc7-a3f9-4605-82a5-1cec58263f6f",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "79dae76d-9e2e-442c-a946-7948c4afae60"
       {:compute-ref #uuid "db14a51e-5e69-4ef3-b334-6fbed8f1b712",
        :exec-duration 11,
        :id "79dae76d-9e2e-442c-a946-7948c4afae60",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "7dd2b67e-352d-400a-9de0-087202a0e907"
       {:compute-ref #uuid "cbd8eb5b-f75e-4566-8a3b-e3b114745516",
        :exec-duration 4,
        :id "7dd2b67e-352d-400a-9de0-087202a0e907",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "7f5fca15-06d1-46d2-936b-50b766b11b83"
       {:compute-ref #uuid "f65936cd-db6c-40e5-aea0-7f1e771af958",
        :exec-duration 441,
        :id "7f5fca15-06d1-46d2-936b-50b766b11b83",
        :kind "code",
        :output-log-lines {:stdout 45},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "82c3d607-5487-439b-9a69-2f18e938929b"
       {:compute-ref #uuid "f80fe423-16fe-41dd-979a-f04253bfa450",
        :exec-duration 117,
        :id "82c3d607-5487-439b-9a69-2f18e938929b",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "83346640-b369-4d5b-8698-5ce6ea21cdd1"
       {:compute-ref #uuid "feb4e0e8-8b8c-4dad-8d23-604b15cb8775",
        :exec-duration 425,
        :id "83346640-b369-4d5b-8698-5ce6ea21cdd1",
        :kind "code",
        :output-log-lines {:stdout 109},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "91c30964-89f5-4cdf-89a1-b85f04cb17cb"
       {:compute-ref #uuid "57a265f8-9e26-44ed-8a82-f53a6e50de46",
        :exec-duration 9,
        :id "91c30964-89f5-4cdf-89a1-b85f04cb17cb",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "9be7df63-a594-451e-bc67-495cf6c8b55d"
       {:compute-ref #uuid "5afa1031-4234-4fb8-b328-95e020b73d51",
        :exec-duration 70,
        :id "9be7df63-a594-451e-bc67-495cf6c8b55d",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "a57ea154-1d58-4179-a401-bb061109363e"
       {:compute-ref #uuid "94465df7-c93d-48ad-b3b7-98279e751b8c",
        :exec-duration 8,
        :id "a57ea154-1d58-4179-a401-bb061109363e",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "aae20034-2697-43c1-8f9f-c8a52c836b30"
       {:compute-ref #uuid "44d26af9-f7e9-4ae6-8a53-b79ecbf65c9e",
        :exec-duration 50,
        :id "aae20034-2697-43c1-8f9f-c8a52c836b30",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "abc8ee32-b0fe-469c-8c04-c70c3f2c569e"
       {:compute-ref #uuid "608be9a7-0838-4849-9e0b-52082175833f",
        :exec-duration 57,
        :id "abc8ee32-b0fe-469c-8c04-c70c3f2c569e",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "af6218fc-c359-4faf-b8ee-da7b5e2a5f18"
       {:compute-ref #uuid "76fc5b31-9c03-4782-9877-e4d4480d45df",
        :exec-duration 25,
        :id "af6218fc-c359-4faf-b8ee-da7b5e2a5f18",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "af906587-480d-4f71-855c-e803e5cba1d5"
       {:compute-ref #uuid "e0da7f46-bd3e-4cfb-8abd-76aa158a8ab1",
        :exec-duration 28,
        :id "af906587-480d-4f71-855c-e803e5cba1d5",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "bfe11b21-7e69-4d77-9a47-6b70b7024d87"
       {:compute-ref #uuid "2e663f6f-49b8-4658-bc25-f6e206342829",
        :exec-duration 17,
        :id "bfe11b21-7e69-4d77-9a47-6b70b7024d87",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "cabc5d67-ea28-4d57-8559-38c4a981c83e"
       {:compute-ref #uuid "4aab1520-16ba-498e-b841-a9b91ff04132",
        :exec-duration 20,
        :id "cabc5d67-ea28-4d57-8559-38c4a981c83e",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f"
       {:compute-ref #uuid "53f2acbb-1917-417a-bc8e-cfd8cf852b1e",
        :exec-duration 74,
        :id "cdec61b8-6039-4c8e-8c67-9ffefdbd0e2f",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "d9f6c457-f4d7-4565-b8d2-0039b3aaf888"
       {:environment
        [:environment
         {:node/id "0149f12a-08de-4f3d-9fd3-4b7a665e8624",
          :article/nextjournal.id
          #uuid "5b45e08b-5b96-413e-84ed-f03b5b65bd66",
          :change/nextjournal.id
          #uuid "6034be04-2bc2-4468-af0e-cd7b9b6e7ed8"}],
        :id "d9f6c457-f4d7-4565-b8d2-0039b3aaf888",
        :kind "runtime",
        :language "python",
        :type :jupyter},
       "db3884f0-fd65-4f9d-9341-918c9e4733cd"
       {:compute-ref #uuid "c5da9add-2648-4c5c-8294-37c617294cd1",
        :exec-duration 425,
        :id "db3884f0-fd65-4f9d-9341-918c9e4733cd",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "db8dcc66-f14b-4344-9205-9c3f9ab20ee6"
       {:compute-ref #uuid "179f65ad-3943-49ea-ab82-2e0fe06e03f3",
        :exec-duration 36,
        :id "db8dcc66-f14b-4344-9205-9c3f9ab20ee6",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "dfae2600-bc53-44b4-a97f-c3758c2b85cd"
       {:compute-ref #uuid "100ec601-af2e-4ace-a9a9-9c4d9ccbc3db",
        :exec-duration 57,
        :id "dfae2600-bc53-44b4-a97f-c3758c2b85cd",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "eaa857a3-9d94-414f-9394-54acd01bf557"
       {:compute-ref #uuid "e6ee6bd3-92e7-4dcf-9423-4fee55f3dd01",
        :exec-duration 19,
        :id "eaa857a3-9d94-414f-9394-54acd01bf557",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "ef06350e-bcee-4e53-ac1f-d9975ed18fc6"
       {:compute-ref #uuid "11b3085f-23b6-40f2-a12e-23cc489b201b",
        :exec-duration 536,
        :id "ef06350e-bcee-4e53-ac1f-d9975ed18fc6",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "f1020f8e-d252-4b90-b78a-e74a366b580e"
       {:compute-ref #uuid "24df8f2f-57ee-456c-b9f3-4ea080fe6eb1",
        :exec-duration 454,
        :id "f1020f8e-d252-4b90-b78a-e74a366b580e",
        :kind "code",
        :output-log-lines {:stdout 2},
        :runtime [:runtime "d9f6c457-f4d7-4565-b8d2-0039b3aaf888"]},
       "f1b41768-cc74-4d27-a958-78929defb755"
       {:compute-ref #uuid "2c59f782-9120-4bda-b145-0165200e3fa8",
        :exec-duration 6,
        :id "f1b41768-cc74-4d27-a958-78929defb755",
        :kind "code",
        :output-log-lines {},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "fe81e0bc-24f9-40d3-a555-f4000eb4ab55"
       {:compute-ref #uuid "4b4c2b41-e070-48d5-b525-54c8a77b97df",
        :exec-duration 324,
        :id "fe81e0bc-24f9-40d3-a555-f4000eb4ab55",
        :kind "code",
        :output-log-lines {:stdout 2},
        :runtime [:runtime "29552ba9-d499-4842-9448-63608ce24e24"]},
       "ffcf0396-b3f9-40e6-a0c2-654401879781"
       {:id "ffcf0396-b3f9-40e6-a0c2-654401879781",
        :kind "code-listing",
        :name "deps.edn"}},
      :nextjournal/id #uuid "77b0a2f9-a708-4e51-8d1d-4393b7bd4a64",
      :article/change
      {:nextjournal/id #uuid "63271681-5796-4a29-a938-65429c974a97"}}}
    
    ```
    </details>
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<tangle file="/Users/brian/Dropbox/Mac/Documents/GitHub/tangledown/examples/asr/genetically-engineered-asr.nextjournal.md">
<!-- #endraw -->

```markdown
<block name="genetically-engineered-asr.nextjournal_2FF0A2"></block>
```

<!-- #raw -->
</tangle>
<!-- #endraw -->
